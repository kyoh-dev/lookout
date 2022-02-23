-- migrate:up
CREATE TABLE public.rec_site
(
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    unique_key TEXT NOT NULL,
    version_date DATE NOT NULL,
    name TEXT NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    disabled_access TEXT,
    access_descr TEXT,
    fee INTEGER,
    comments TEXT,
    maintained_by TEXT,
    closed_status TEXT,
    closed_descr TEXT,
    closed_on TIMESTAMP WITHOUT TIME ZONE,
    reopen_on TIMESTAMP WITHOUT TIME ZONE,
    closed_reason TEXT,
    camping BOOLEAN,
    camping_descr TEXT,
    campervanning BOOLEAN,
    campervanning_descr TEXT,
    campervan_type TEXT,
    trail_bike_area BOOLEAN,
    trail_bike_area_descr TEXT,
    heritage BOOLEAN,
    heritage_descr TEXT,
    fishing BOOLEAN,
    fishing_descr TEXT,
    fossicking BOOLEAN,
    fossicking_descr TEXT,
    hang_gliding BOOLEAN,
    hang_gliding_descr TEXT,
    horse_riding BOOLEAN,
    horse_riding_descr TEXT,
    paddling BOOLEAN,
    paddling_descr TEXT,
    picnicing BOOLEAN,
    picnicing_descr TEXT,
    noise_warning BOOLEAN,
    noise_warning_descr TEXT,
    rock_climbing BOOLEAN,
    rock_climbing_descr TEXT,
    dog_walking BOOLEAN,
    dog_walking_descr TEXT,
    wildlife BOOLEAN,
    wildlife_descr TEXT,
    num_bbq_electric INTEGER,
    num_bbq_pit INTEGER,
    num_bbq_gas INTEGER,
    num_bbq_wood INTEGER,
    rep_point GEOMETRY(POINT, 7844) NOT NULL,
    CONSTRAINT rec_sites_unique_key_unique
        UNIQUE (unique_key)
);

-- migrate:down
DROP TABLE public.rec_site;