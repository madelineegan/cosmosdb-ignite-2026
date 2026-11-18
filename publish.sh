#!/usr/bin/env bash
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required." >&2
  exit 1
fi

gh auth status >/dev/null
OWNER="${GH_OWNER:-$(gh api user --jq .login)}"
REPO="${GH_REPO:-cosmosdb-ignite-2026-brk367}"

if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  echo "Repository $OWNER/$REPO already exists. Refusing to overwrite it." >&2
  exit 1
fi

if [ ! -d .git ]; then
  git init -b main
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "Create BRK367 Azure Cosmos DB resource page"
fi

gh repo create "$OWNER/$REPO" --public --source=. --remote=origin --push

echo
printf 'Repository: https://github.com/%s/%s\n' "$OWNER" "$REPO"
printf 'Expected Pages URL after deployment: https://%s.github.io/%s/\n' "$OWNER" "$REPO"
echo "Next: enable GitHub Actions as the Pages source if it is not enabled automatically."
