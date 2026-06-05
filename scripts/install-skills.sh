#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/skills"
TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/skills"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "No skills directory found at $SOURCE_DIR"
  exit 1
fi

mkdir -p "$TARGET_DIR"
BACKUP_DIR="$TARGET_DIR/.backups"

for skill_dir in "$SOURCE_DIR"/*; do
  [ -d "$skill_dir" ] || continue
  skill_name="$(basename "$skill_dir")"
  target_path="$TARGET_DIR/$skill_name"

  if [ -e "$target_path" ]; then
    mkdir -p "$BACKUP_DIR"
    backup_path="$BACKUP_DIR/$skill_name-$(date +%Y%m%d-%H%M%S)"
    mv "$target_path" "$backup_path"
    echo "Backed up existing $skill_name to $backup_path"
  fi

  cp -R "$skill_dir" "$target_path"
  echo "Installed $skill_name to $target_path"
done

echo "Done."
