from load.common import DataSchema

PARK_SCHEMA = DataSchema(
    schema_map={
        "NAME": "name",
        "AREA_TYPE": "type",
        "AREASQM": "area_sqm",
        "HECTARES": "hectares",
        "MANAGER": "managed_by",
        "IUCN": "iucn_code",
        "ESTAB_DATE": "established_date",
        "LAST_MOD": "modified_date",
        "VERS_DATE": "version_date",
    },
    uppercase_attributes={"AREA_TYPE"},
)
