select
  vers_date as versioned_at,
  name,
  latitude,
  longitude,
  dis_access as disabled_access,
  access_dsc as directions,
  case when fee is null
    then 0
    else fee::int
  end as fee,
  maintained_by,
  clos_stat as closure_status,
  clos_desc as closure_descr,
  clos_reas as closure_reason,
  shape as geometry

from {{ source('datashare', 'datashare__rec_site') }}
