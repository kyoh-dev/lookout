{{ config(
  indexes=[
    {'columns': ['geometry'], 'type': 'gist'}
  ],
  post_hook='alter table {{ this }} add primary key (id)'
)}}

select * from {{ ref('stg_datashare__park') }}
