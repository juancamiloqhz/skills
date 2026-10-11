#!/usr/bin/env python3
"""Resolve a jstack role through its discovered setup skill without dispatching."""

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def config_path(explicit=None):
    if explicit:
        return Path(explicit).expanduser()
    if os.environ.get("JSTACK_CONFIG"):
        return Path(os.environ["JSTACK_CONFIG"]).expanduser()
    root = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config")
    return root / "jstack" / "models.json"


def preflight(setup_skill, config, catalog_path, role):
    setup = Path(setup_skill).expanduser().resolve()
    entry = (setup / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = entry.split("---", 2)
    if (not entry.startswith("---\n") or len(frontmatter) != 3
            or not re.search(r'^name:\s*[\'\"]?setup-jstack[\'\"]?\s*$',
                             frontmatter[1], re.MULTILINE)):
        raise ValueError("--setup-skill must be the catalog-discovered setup-jstack directory")
    resolver = setup / "scripts" / "models.py"
    if not resolver.is_file():
        raise ValueError(f"missing setup-jstack resolver: {resolver}")
    result = subprocess.run([
        sys.executable, str(resolver), "resolve", str(config),
        "--catalog", str(catalog_path), "--role", role,
    ], capture_output=True, text=True, check=False)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "setup-jstack resolution failed")
    targets = json.loads(result.stdout)
    if not isinstance(targets, list) or not targets:
        raise ValueError("setup-jstack returned no ordered targets")
    catalog = json.loads(Path(catalog_path).expanduser().read_text(encoding="utf-8"))
    parent = catalog.get("inheritedProviderInstanceId")
    providers = {p["providerInstanceId"]: p for p in catalog["providers"]}
    kind = ("pool" if role == "arena cross-judge pool" else "panel"
            if role in {"arena runners", "architect runners", "interrogate reviewers"}
            else "scalar")
    identities, availability = [], []
    for target in targets:
        inherited = target is None
        pid = parent if inherited else target["providerInstanceId"]
        model = catalog.get("inheritedModel") if inherited else target["model"]
        provider = providers.get(pid)
        reason = None
        if (not provider or provider.get("canRunChildTask") is not True
                or not model or model not in {m["id"] for m in provider.get("models", [])}):
            reason = f"effective child selection unavailable: {pid!r}/{model!r}"
        elif pid != parent and provider.get("canRunCrossProviderChildTask") is not True:
            reason = f"cross-provider child execution unavailable on {pid!r}"
        if reason and kind != "pool":
            raise ValueError(f"{role}: {reason}")
        identities.append({"providerInstanceId": pid, "model": model, "inherited": inherited})
        availability.append({"canDispatch": reason is None, "reason": reason})
    if kind == "pool" and not any(seat["canDispatch"] for seat in availability):
        reasons = "; ".join(seat["reason"] for seat in availability)
        raise ValueError(f"{role}: no executable judge alternative: {reasons}")
    return {"role": role, "selectionKind": kind, "targets": targets,
            "effectiveIdentities": identities, "availability": availability,
            "resolver": str(resolver),
            "config": str(Path(config).expanduser().resolve())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--setup-skill", required=True)
    parser.add_argument("--catalog", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--config")
    args = parser.parse_args()
    try:
        result = preflight(args.setup_skill, config_path(args.config), args.catalog, args.role)
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"juan-mode: {error}\n")


if __name__ == "__main__":
    main()
