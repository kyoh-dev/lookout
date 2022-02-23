-- migrate:up
CREATE TABLE public.park
(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    type TEXT,
    area_sqm NUMERIC(20, 2),
    hectares NUMERIC(16, 2),
    managed_by TEXT,
    iucn_code TEXT,
    established_date DATE,
    modified_date DATE,
    version_date DATE,
    geometry GEOMETRY(MULTIPOLYGON, 7844) NOT NULL
);

-- migrate:down
DROP TABLE public.park;
