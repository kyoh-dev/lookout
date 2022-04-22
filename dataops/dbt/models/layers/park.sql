{{ config(
  indexes=[
    {'columns': ['geometry'], 'type': 'gist'}
  ],
  post_hook='alter table {{ this }} add primary key (id)'
)}}

with dissolved as (

  select
    site_id,
    st_multi(st_union(geometry)) as geometry,
    sum(hectares) as hectares

  from {{ ref('stg_datashare__park') }}

  group by site_id

),

final as (

  select
    stg.id,
    dissolved.site_id,
    stg.name,
    stg.name_short,
    stg.type,
    stg.total_area,
    stg.maintained_by,
    stg.veac_study,
    stg.iucn_code,
    stg.established_at,
    stg.modified_at,
    stg.versioned_at,
    dissolved.hectares,
    dissolved.geometry

  from dissolved
  inner join {{ ref('stg_datashare__park') }} as stg
    on dissolved.site_id = stg.site_id

)

select * from final
