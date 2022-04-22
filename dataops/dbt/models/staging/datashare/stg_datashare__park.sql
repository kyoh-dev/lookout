select
  objectid as id,
  prims_id as site_id,
  name,
  name_short,
  area_type as type,
  total_area,
  manager as maintained_by,
  veac_study,
  upper(iucn) as iucn_code,
  estab_date as established_at,
  last_mod as modified_at,
  vers_date as versioned_at,
  areasqm as area_sqm,
  hectares,
  shape as geometry

from {{ source('datashare', 'datashare__park') }}
