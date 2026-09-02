#!/usr/bin/env python3
"""Inventory repository-owned agent instruction files and local references."""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import unquote


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "target",
    "vendor",
}
PRIMARY_NAMES = {
    "AGENTS.md",
    "AGENTS.override.md",
    "CLAUDE.md",
    "CLAUDE.local.md",
}
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"(`+)([^`\n]+?)\1")
CLAUDE_IMPORT_RE = re.compile(
    r"(?<![\w`])@((?:~|\.{0,2}/)?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*)"
)
CODE_PATH_PREFIXES = (
    ".claude/",
    ".codex/",
    "data/",
    "docs/",
    "drizzle/",
    "node_modules/",
    "public/",
    "scripts/",
    "src/",
)
CODE_PATH_SUFFIXES = {".cjs", ".js", ".json", ".jsx", ".md", ".mdx", ".mjs", ".ts", ".tsx"}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument(
        "--cwd",
        type=Path,
        help="Working directory used to model the Codex project chain (default: root)",
    )
    parser.add_argument(
        "--fallback-name",
        action="append",
        default=[],
        help="Configured Codex fallback filename; may be repeated",
    )
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser.parse_args(argv)


def within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def validate_fallback_names(names: Iterable[str]) -> list[str]:
    result: list[str] = []
    for name in names:
        if not name or Path(name).name != name or name in {".", ".."}:
            raise ValueError(f"fallback names must be plain filenames: {name!r}")
        if name not in result:
            result.append(name)
    return result


def markdown_without_fences(text: str) -> str:
    output: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        stripped = line.lstrip()
        marker = stripped[:3]
        if marker in {"```", "~~~"}:
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            output.append(line)
    return "\n".join(output)


def visible_markdown(text: str) -> str:
    """Remove fenced and inline code so examples are not treated as imports."""
    return INLINE_CODE_RE.sub("", markdown_without_fences(text))


def is_instruction_file(path: Path, root: Path, fallback_names: set[str]) -> bool:
    if path.name in PRIMARY_NAMES or path.name in fallback_names:
        return True
    rel_parts = path.relative_to(root).parts
    return (
        path.suffix.lower() == ".md"
        and ".claude" in rel_parts
        and "rules" in rel_parts
        and rel_parts.index(".claude") < rel_parts.index("rules")
    )


def iter_instruction_files(root: Path, fallback_names: set[str]) -> Iterable[Path]:
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        base = Path(directory)
        for filename in sorted(files):
            path = base / filename
            if is_instruction_file(path, root, fallback_names):
                yield path


def normalize_reference(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    return unquote(target.split("#", 1)[0])


def reference_record(
    source: Path,
    root: Path,
    syntax: str,
    raw: str,
    *,
    allow_root_fallback: bool = False,
) -> dict[str, str]:
    target = normalize_reference(raw)
    record = {"syntax": syntax, "target": target}
    if not target:
        return {**record, "status": "anchor-only"}
    if target.startswith(("http://", "https://", "mailto:", "data:", "file:")):
        return {**record, "status": "external"}
    if target.startswith("~"):
        return {**record, "status": "outside-repository"}

    candidates = [source.parent / target]
    if allow_root_fallback and source.parent != root:
        candidates.append(root / target)

    first_local: Path | None = None
    for candidate in candidates:
        resolved = candidate.resolve(strict=False)
        if not within(resolved, root):
            continue
        first_local = first_local or resolved
        if resolved.exists():
            return {
                **record,
                "status": "exists",
                "resolved": resolved.relative_to(root).as_posix(),
            }

    if first_local:
        return {
            **record,
            "status": "missing",
            "resolved": first_local.relative_to(root).as_posix(),
        }
    return {**record, "status": "outside-repository"}


def looks_like_code_path(raw: str) -> bool:
    target = raw.strip()
    if not target or any(character.isspace() for character in target):
        return False
    if target.startswith(("/", "@", "http://", "https://")):
        return False
    if target.startswith(("./", "../", "~/")):
        return True
    if target.startswith(CODE_PATH_PREFIXES):
        return True
    if target.startswith(".") and "/" in target:
        return True
    return Path(target.rstrip("/")).suffix.lower() in CODE_PATH_SUFFIXES


def code_path_record(source: Path, root: Path, raw: str) -> dict[str, str] | None:
    target = raw.strip()
    if not looks_like_code_path(target):
        return None
    literal = reference_record(
        source,
        root,
        "inline-code-path",
        target,
        allow_root_fallback=True,
    )
    if literal["status"] != "missing" or not any(
        character in target for character in "*?["
    ):
        return literal
    for base in (source.parent, root):
        matches = sorted(glob.glob(str(base / target)))
        for match in matches:
            resolved = Path(match).resolve(strict=False)
            if within(resolved, root):
                return {
                    "syntax": "inline-code-path",
                    "target": target,
                    "status": "exists",
                    "resolved": resolved.relative_to(root).as_posix(),
                }
    return literal


def collect_references(path: Path, root: Path, text: str) -> list[dict[str, str]]:
    unfenced = markdown_without_fences(text)
    visible = INLINE_CODE_RE.sub("", unfenced)
    refs = [
        reference_record(path, root, "markdown-link", match.group(1))
        for match in MARKDOWN_LINK_RE.finditer(visible)
    ]
    if path.name in {"CLAUDE.md", "CLAUDE.local.md"}:
        refs.extend(
            reference_record(path, root, "claude-import", match.group(1))
            for match in CLAUDE_IMPORT_RE.finditer(visible)
        )
    refs.extend(
        record
        for match in INLINE_CODE_RE.finditer(unfenced)
        if (record := code_path_record(path, root, match.group(2))) is not None
    )
    return refs


def classify(path: Path, root: Path, fallback_names: set[str]) -> str:
    rel_parts = path.relative_to(root).parts
    if ".claude" in rel_parts and "rules" in rel_parts:
        return "claude-rule"
    if path.name == "AGENTS.override.md":
        return "codex-override"
    if path.name == "AGENTS.md":
        return "codex"
    if path.name in {"CLAUDE.md", "CLAUDE.local.md"}:
        return "claude"
    if path.name in fallback_names:
        return "codex-fallback"
    return "unknown"


def read_repository_text(path: Path, root: Path) -> tuple[str, str | None]:
    if path.is_symlink() and not within(path.resolve(strict=False), root):
        return "", "symlink target is outside the repository"
    try:
        return path.read_text(encoding="utf-8"), None
    except (OSError, UnicodeError) as exc:
        return "", str(exc)


def inspect_file(path: Path, root: Path, fallback_names: set[str]) -> dict[str, Any]:
    relative = path.relative_to(root).as_posix()
    text, error = read_repository_text(path, root)
    result: dict[str, Any] = {
        "path": relative,
        "kind": classify(path, root, fallback_names),
        "bytes": len(text.encode("utf-8")),
        "lines": len(text.splitlines()),
        "empty": not text.strip(),
        "symlink": path.is_symlink(),
        "references": collect_references(path, root, text) if not error else [],
    }
    if path.is_symlink():
        result["symlink_target"] = os.readlink(path)
    if error:
        result["error"] = error
    return result


def directory_chain(root: Path, cwd: Path) -> list[Path]:
    chain = [root]
    current = root
    for part in cwd.relative_to(root).parts:
        current = current / part
        chain.append(current)
    return chain


def nonempty_file(path: Path, root: Path) -> bool:
    if not path.exists() and not path.is_symlink():
        return False
    text, error = read_repository_text(path, root)
    return error is None and bool(text.strip())


def codex_chain(root: Path, cwd: Path, fallback_names: list[str]) -> list[dict[str, Any]]:
    names = ["AGENTS.override.md", "AGENTS.md", *fallback_names]
    result: list[dict[str, Any]] = []
    for directory in directory_chain(root, cwd):
        for name in names:
            candidate = directory / name
            if nonempty_file(candidate, root):
                text, _ = read_repository_text(candidate, root)
                result.append(
                    {
                        "path": candidate.relative_to(root).as_posix(),
                        "bytes": len(text.encode("utf-8")),
                    }
                )
                break
    return result


def claude_ancestor_candidates(root: Path, cwd: Path) -> list[str]:
    result: list[str] = []
    for directory in directory_chain(root, cwd):
        candidates = [directory / "CLAUDE.md", directory / "CLAUDE.local.md"]
        if directory == root:
            candidates.insert(1, directory / ".claude" / "CLAUDE.md")
        for candidate in candidates:
            if nonempty_file(candidate, root):
                result.append(candidate.relative_to(root).as_posix())
    return result


def build_inventory(root: Path, cwd: Path, fallback_names: list[str]) -> dict[str, Any]:
    fallback_set = set(fallback_names)
    files = [inspect_file(path, root, fallback_set) for path in iter_instruction_files(root, fallback_set)]
    chain = codex_chain(root, cwd, fallback_names)
    broken = [
        {"source": item["path"], **reference}
        for item in files
        for reference in item["references"]
        if reference["status"] == "missing"
    ]
    warnings = [
        {"source": item["path"], "warning": item["error"]}
        for item in files
        if "error" in item
    ]
    total = sum(item["bytes"] for item in chain)
    return {
        "root": str(root),
        "cwd": str(cwd),
        "files": files,
        "codex_project_chain": chain,
        "codex_project_bytes": total,
        "codex_default_limit_risk": total > 32 * 1024,
        "claude_ancestor_candidates": claude_ancestor_candidates(root, cwd),
        "broken_references": broken,
        "loading_warnings": warnings,
    }


def escape_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_markdown(data: dict[str, Any]) -> str:
    lines = [
        "# Agent instruction inventory",
        "",
        f"- Root: `{data['root']}`",
        f"- Working directory: `{data['cwd']}`",
        "",
        "## Files",
        "",
    ]
    if data["files"]:
        lines.extend(
            [
                "| Path | Kind | Lines | Bytes | Symlink |",
                "| --- | --- | ---: | ---: | --- |",
            ]
        )
        for item in data["files"]:
            lines.append(
                "| {path} | {kind} | {lines} | {bytes} | {symlink} |".format(
                    **{key: escape_cell(value) for key, value in item.items() if key != "references"}
                )
            )
    else:
        lines.append("No repository-owned instruction files found.")

    lines.extend(["", "## Codex project chain (default semantics)", ""])
    if data["codex_project_chain"]:
        lines.extend(f"- `{item['path']}` ({item['bytes']} bytes)" for item in data["codex_project_chain"])
    else:
        lines.append("No project instruction file would load from this working directory.")
    lines.append(
        f"- Combined bytes: {data['codex_project_bytes']} "
        f"(default limit risk: {data['codex_default_limit_risk']})"
    )

    lines.extend(["", "## Claude ancestor candidates", ""])
    if data["claude_ancestor_candidates"]:
        lines.extend(f"- `{path}`" for path in data["claude_ancestor_candidates"])
    else:
        lines.append("No ancestor candidate found.")

    lines.extend(["", "## Broken local references", ""])
    if data["broken_references"]:
        lines.extend(
            f"- `{item['source']}` → `{item['target']}` ({item['syntax']})"
            for item in data["broken_references"]
        )
    else:
        lines.append("None detected.")

    lines.extend(["", "## Loading warnings", ""])
    if data["loading_warnings"]:
        lines.extend(
            f"- `{item['source']}`: {item['warning']}"
            for item in data["loading_warnings"]
        )
    else:
        lines.append("None detected.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    cwd = (args.cwd or root).resolve()
    try:
        fallback_names = validate_fallback_names(args.fallback_name)
        if not root.is_dir():
            raise ValueError(f"root is not a directory: {root}")
        if not cwd.is_dir():
            raise ValueError(f"cwd is not a directory: {cwd}")
        if not within(cwd, root):
            raise ValueError(f"cwd must be inside root: {cwd}")
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    data = build_inventory(root, cwd, fallback_names)
    if args.format == "json":
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print(render_markdown(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
