#!/usr/bin/env bash
set -euo pipefail
scene_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
: "${ISAAC_SIM_ROOT:?Set ISAAC_SIM_ROOT to your Isaac Sim installation directory}"
unset PYTHONPATH LD_LIBRARY_PATH CONDA_PREFIX VIRTUAL_ENV
export PYTHONNOUSERSITE=1
exec "$ISAAC_SIM_ROOT/python.sh" "$scene_dir/scripts/open_scene.py" "$@"
