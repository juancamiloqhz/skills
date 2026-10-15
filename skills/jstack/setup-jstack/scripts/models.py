#!/usr/bin/env python3
"""Validate, save and resolve jstack selections using a live T3 Code catalog."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile


ROLES = (
    "feature, refactoring", "bug-fix", "perf-issue", "hillclimb",
    "judgment and prose", "hardest tasks", "how explorer", "how explainer",
    "why investigators", "why synthesizer", "reflect tooling",
    "reflect judgment, divergent, synthesizer", "arena runners",
    "arena cross-judge pool", "swarm workers", "architect runners",
    "interrogate reviewers",
)
PANEL_ROLES = frozenset(("arena runners", "architect runners", "interrogate reviewers"))
LIST_ROLES = PANEL_ROLES | {"arena cross-judge pool"}
PRESETS = {"small": "medium", "medium": "high", "large": "xhigh", "unlimited": "max"}


def absolute_path(path):
    # Keep symlink/.. traversal in the order the filesystem will interpret it.
    return Path(path).expanduser().absolute()


def path_present(path):
    try:
        path.lstat()
        return True
    except FileNotFoundError:
        return False


def project_directory(explicit=None):
    if explicit is not None:
        root = absolute_path(explicit)
        require(root.is_dir(), f"project root is not a directory: {root}")
        return root
    try:
        result = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                capture_output=True, text=True, check=False,
                                env=dict(os.environ, LC_ALL="C"))
    except FileNotFoundError:
        return None
    if result.returncode == 0:
        return absolute_path(result.stdout.rstrip("\n"))
    if "not a git repository" in result.stderr:
        return None
    raise ValueError(f"cannot discover project root: {result.stderr.strip()}")


def locate_config(explicit=None, project_root=None, scope=None):
    require(scope in (None, "global", "project"), "unknown configuration scope")
    require(not (scope and explicit is not None), "scope and explicit config are mutually exclusive")
    global_path = absolute_path(Path(os.environ.get("XDG_CONFIG_HOME")
                                     or Path.home() / ".config") / "jstack" / "models.json")
    if scope == "global":
        path, source = global_path, "global"
    elif explicit is not None:
        path, source = absolute_path(explicit), "explicit"
    elif scope is None and os.environ.get("JSTACK_CONFIG"):
        path, source = absolute_path(os.environ["JSTACK_CONFIG"]), "environment"
    else:
        root = project_directory(project_root)
        require(scope != "project" or root is not None,
                "project scope requires --project-root or a Git checkout")
        project_path = root / ".jstack" / "models.json" if root else None
        if project_path is not None and (scope == "project" or path_present(project_path)):
            path, source = project_path, "project"
        else:
            path, source = global_path, "global"
    return {"path": str(path), "source": source, "exists": path_present(path)}


def template(preset):
    return {
        "schemaVersion": 1,
        "preset": preset,
        "roles": {
            role: [{"alias": "inherit-parent"} for _ in range(2 if role in PANEL_ROLES else 1)]
            if role in LIST_ROLES
            else {"alias": "inherit-parent"}
            for role in ROLES
        },
    }


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_seat(seat, providers, label):
    require(isinstance(seat, dict), f"{label}: expected a seat object")
    if "alias" in seat:
        require(seat == {"alias": "inherit-parent"}, f"{label}: invalid inheritance alias")
        return
    require(set(seat) == {"providerInstanceId", "model", "options"},
            f"{label}: concrete seat needs providerInstanceId, model and options only")
    pid, mid, options = seat["providerInstanceId"], seat["model"], seat["options"]
    require(isinstance(pid, str) and isinstance(mid, str), f"{label}: IDs must be strings")
    provider = providers.get(pid)
    require(provider is not None and provider.get("canRunChildTask") is True,
            f"{label}: unavailable provider {pid!r}")
    model = next((m for m in provider.get("models", []) if m["id"] == mid), None)
    require(model is not None, f"{label}: unavailable model {mid!r} on {pid!r}")
    require(isinstance(options, dict), f"{label}: options must be an object")
    advertised = {opt["id"]: opt for opt in model.get("options") or []}
    for key, value in options.items():
        opt = advertised.get(key)
        require(opt is not None, f"{label}: unadvertised option {key!r}")
        if opt["type"] == "boolean":
            require(type(value) is bool, f"{label}: {key} requires a boolean")
        elif opt["type"] == "select":
            require(isinstance(value, str) and value in [v["id"] for v in opt["options"]],
                    f"{label}: unsupported {key} value {value!r}")
        else:
            raise ValueError(f"{label}: unsupported catalog option type {opt['type']!r}")


def validate(config, catalog):
    require(isinstance(config, dict), "configuration must be an object")
    require(set(config) == {"schemaVersion", "preset", "roles"}, "unexpected configuration fields")
    require(type(config["schemaVersion"]) is int and config["schemaVersion"] == 1,
            "unsupported schemaVersion")
    require(isinstance(config["preset"], str) and config["preset"] in PRESETS,
            "unknown reasoning preset")
    require(isinstance(catalog, dict) and isinstance(catalog.get("providers"), list),
            "catalog must be the unwrapped capabilities payload")
    providers = {p["providerInstanceId"]: p for p in catalog["providers"]}
    roles = config["roles"]
    require(isinstance(roles, dict), "roles must be an object")
    require(set(roles) == set(ROLES),
            f"role mismatch: missing={sorted(set(ROLES)-set(roles))}, extra={sorted(set(roles)-set(ROLES))}")
    for role, value in roles.items():
        if role in LIST_ROLES:
            require(isinstance(value, list) and bool(value), f"{role}: expected a nonempty seat list")
            for index, seat in enumerate(value):
                validate_seat(seat, providers, f"{role}[{index}]")
        else:
            validate_seat(value, providers, role)
    return config


def resolve(config, role):
    require(role in ROLES, f"unknown role {role!r}")
    seats = config["roles"][role]
    if role not in LIST_ROLES:
        seats = [seats]
    return [None if "alias" in seat else dict(seat) for seat in seats]


def atomic_write(path, config):
    path = Path(path).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False,
                                         encoding="utf-8") as handle:
            temporary = handle.name
            json.dump(config, handle, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary and os.path.exists(temporary):
            os.unlink(temporary)


def read_json(path):
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"duplicate JSON key {key!r}")
            result[key] = value
        return result
    return json.loads(Path(path).expanduser().read_text(encoding="utf-8"),
                      object_pairs_hook=unique_pairs)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    draft = commands.add_parser("template")
    draft.add_argument("--preset", choices=PRESETS, default="medium")
    locator = commands.add_parser("locate")
    selection = locator.add_mutually_exclusive_group()
    selection.add_argument("--config")
    selection.add_argument("--scope", choices=("global", "project"))
    locator.add_argument("--project-root")
    for name in ("validate", "write", "resolve"):
        sub = commands.add_parser(name)
        sub.add_argument("config", nargs="?" if name == "resolve" else None)
        sub.add_argument("--catalog", required=True)
        if name == "write":
            sub.add_argument("--output", required=True)
        if name == "resolve":
            sub.add_argument("--role", required=True, choices=ROLES)
            sub.add_argument("--project-root")
            sub.add_argument("--with-source", action="store_true")
            sub.add_argument("--worker-override", help="task-local Swarm seat JSON; never saved")
    args = parser.parse_args()
    try:
        if args.command == "template":
            result = template(args.preset)
        elif args.command == "locate":
            result = locate_config(args.config, args.project_root, args.scope)
        else:
            location = (locate_config(args.config, args.project_root)
                        if args.command == "resolve" else {"path": args.config})
            try:
                catalog = read_json(args.catalog)
                config = validate(read_json(location["path"]), catalog)
            except (ValueError, OSError, KeyError, TypeError) as error:
                raise ValueError(f"configuration {location['path']}: {error}") from error
            if args.command == "write":
                atomic_write(args.output, config)
                result = {"written": str(Path(args.output).expanduser())}
            elif args.command == "resolve":
                result = resolve(config, args.role)
                if args.worker_override is not None:
                    require(args.role == "swarm workers", "worker override requires the swarm workers role")
                    seat = read_json(args.worker_override)
                    providers = {p["providerInstanceId"]: p for p in catalog["providers"]}
                    validate_seat(seat, providers, "worker override")
                    result = [None if "alias" in seat else dict(seat)]
                if args.with_source:
                    result = {"config": location["path"], "configSource": location["source"],
                              "targets": result}
            else:
                result = {"valid": True, "roles": len(ROLES)}
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"jstack: {error}\n")


if __name__ == "__main__":
    main()
