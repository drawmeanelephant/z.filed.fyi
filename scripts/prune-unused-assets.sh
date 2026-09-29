#!/bin/sh
# Remove default runtime assets that the la-famille build fills in but this
# theme does not reference. Only deletes files with zero references in public/.
set -eu
cd "$(dirname "$0")/.."
PUB=public
for f in assets/css/theme.css assets/css/theme-foundations.css \
         assets/css/layout-editorial.css assets/css/layout-midnight.css \
         assets/css/layout-terminal.css assets/css/search.css \
         assets/img/mascot-default.jpeg assets/img/jules-logo.png \
         assets/img/u1f419_u1f354.png; do
  if [ -f "$PUB/$f" ]; then
    base=$(basename "$f")
    if ! grep -rq "$base" "$PUB" --include='*.html' --include='*.css' --include='*.js' --include='*.json' 2>/dev/null; then
      rm "$PUB/$f"
      echo "pruned: $f"
    else
      echo "kept (referenced): $f"
    fi
  fi
done
