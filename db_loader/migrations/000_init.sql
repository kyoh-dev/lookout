-- migrate:up
SET client_encoding = 'UTF8';

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA PUBLIC;

--migrate:down
DROP EXTENSION postgis;
