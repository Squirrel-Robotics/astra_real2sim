#!/usr/bin/env bash
set -euo pipefail
scene_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
blender_bin="${BLENDER_BIN:-blender}"
exec "$blender_bin" "$scene_dir/leju_workbench_aligned.blend" "$@"
