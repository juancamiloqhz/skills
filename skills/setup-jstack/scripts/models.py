#!/usr/bin/env python3
"""Validate, save and resolve jstack selections using a live T3 catalog."""

import argparse
import json
import os
from pathlib import Path
import tempfile


ROLES = (
    "feature, refactoring", "bug-fix", "perf-issue", "hillclimb",
    "judgment and prose", "hardest tasks", "how explorer", "how explainer",
    "why investigators", "why synthesizer", "reflect tooling",
    "reflect judgment, divergent, synthesizer", "arena runners",
    "arena cross-judge pool", "swarm workers", "architect runners",
    "interrogate reviewers",
)
LIST_ROLES = frozenset((
    "arena runners", "arena cross-judge pool", "architect runners",
    "interrogate reviewers",
))
PRESETS = {"small": "medium", "medium": "high", "large": "xhigh", "unlimited": "max"}


def template(preset):
    return {
        "schemaVersion": 1,
        "preset": preset,
        "roles": {
            role: [{"alias": "inherit-parent"}] if role in LIST_ROLES
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
    for name in ("validate", "write", "resolve"):
        sub = commands.add_parser(name)
        sub.add_argument("config")
        sub.add_argument("--catalog", required=True)
        if name == "write":
            sub.add_argument("--output", required=True)
        if name == "resolve":
            sub.add_argument("--role", required=True, choices=ROLES)
    args = parser.parse_args()
    try:
        if args.command == "template":
            result = template(args.preset)
        else:
            config = validate(read_json(args.config), read_json(args.catalog))
            if args.command == "write":
                atomic_write(args.output, config)
                result = {"written": str(Path(args.output).expanduser())}
            elif args.command == "resolve":
                result = resolve(config, args.role)
            else:
                result = {"valid": True, "roles": len(ROLES)}
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"jstack: {error}\n")


if __name__ == "__main__":
    main()
