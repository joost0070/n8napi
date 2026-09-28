#!/usr/bin/env bash
# Dagelijkse run van de voorraadradar: ophalen -> radar -> overzichtspagina.
# Gebruik:  bash voorraad-watch/scripts/dagelijks.sh      (datamap: $RADAR_DATA of /tmp/radar-<datum>)
set -euo pipefail
HIER="$(cd "$(dirname "$0")" && pwd)"
export RADAR_DATA="${RADAR_DATA:-/tmp/radar-$(date +%F)}"
mkdir -p "$RADAR_DATA" && cd "$RADAR_DATA"
python3 "$HIER/ophalen.py" 2>&1 | tee ophalen.log
python3 "$HIER/uitverkoop.py" 2>&1 | tee radar.txt
python3 "$HIER/pagina.py"
echo "KLAAR: $RADAR_DATA/voorraadradar.html"
