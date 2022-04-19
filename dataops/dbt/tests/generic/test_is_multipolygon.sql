{% test is_multipolygon(model, column_name) %}

select *
from {{ model }}
where st_geometrytype({{ column_name }}) <> 'ST_MultiPolygon'

{% endtest %}
