select
  objectid as id,
  name as site_name,
  name_short as site_name_short,
  area_type as type,
  total_area,
  manager as site_manager,
  veac_study,
  upper(iucn) as iucn_code,
  estab_date as established_at,
  last_mod as modified_at,
  vers_date as versioned_at,
  areasqm as area_sqm,
  hectares,
  shape as geometry

from {{ source('datashare', 'park') }}
