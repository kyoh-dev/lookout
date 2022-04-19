#!/usr/bin/env bash

set -eu

if [ $# -ne 2 ]; then
  echo "Both table and filepath are required arguments"
else
  TABLE=$1
  FILEPATH=$2
fi

PG_CONN="PG:host=${PG_HOST} port=${PG_PORT} dbname=${PG_DBNAME} user=${PG_USER} password=${PG_PASSWORD}"

ogr2ogr -progress -overwrite -f "PostgreSQL" "${PG_CONN}" "$FILEPATH" \
  -nln "$TABLE" -nlt PROMOTE_TO_MULTI \
  --config PG_USE_COPY YES --config OGR_TRUNCATE YES
