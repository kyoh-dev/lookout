-- migrate:up
SET client_encoding = 'UTF8';

CREATE EXTENSION postgis;
CREATE SCHEMA layers;

--migrate:down
DROP SCHEMA layers;
DROP EXTENSION postgis;
