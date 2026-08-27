#!/usr/bin/env bash
# Propaga .claude/commands/vegapunk/agents/*.md (fonte da verdade) para: ~/.claude/commands, FURY e plugin/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/.claude/commands/vegapunk/agents"
FURY=/home/crazu/projetos/FURY
cp "$SRC/stella.md" "$ROOT/.claude/commands/vegapunk.md"
for dst in "$HOME/.claude/commands" "$FURY/.claude/commands"; do
  mkdir -p "$dst/vegapunk/agents"; cp "$SRC"/*.md "$dst/vegapunk/agents/"; cp "$SRC/stella.md" "$dst/vegapunk.md"
  [ -d "$ROOT/.claude/commands/vegapunk/workflows" ] && { mkdir -p "$dst/vegapunk/workflows"; cp "$ROOT"/.claude/commands/vegapunk/workflows/* "$dst/vegapunk/workflows/"; }
done
mkdir -p "$FURY/squads/vegapunk"; rsync -a --delete --exclude _work "$ROOT/squads/vegapunk/" "$FURY/squads/vegapunk/"
for f in "$SRC"/*.md; do
  id=$(basename "$f" .md); skill="$ROOT/plugin/vegapunk-satellites/skills/$id/SKILL.md"
  [ -f "$skill" ] || continue
  { sed -n '1,/^---$/p' "$skill" | sed '1d' | sed '$d' | { echo '---'; cat; echo '---'; }; echo; tail -n +2 "$f"; } > "$skill.tmp" && mv "$skill.tmp" "$skill"
done
echo "sincronizado: global, FURY, plugin"
