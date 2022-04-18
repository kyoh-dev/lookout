#!/usr/bin/env bash

set -eu

PG_CONN="PG:host=${PG_HOST} port=${PG_PORT} dbname=${PG_DBNAME} user=${PG_USER} password=${PG_PASSWORD}"

ogr2ogr -progress -overwrite -f "PostgreSQL" "${PG_CONN}" "/data/recsite.gdb" \
  -nln staging.rec_site -nlt PROMOTE_TO_MULTI \
  --config PG_USE_COPY YES --config OGR_TRUNCATE YES
