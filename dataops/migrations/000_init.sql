-- migrate:up
SET client_encoding = 'UTF8';

CREATE EXTENSION postgis;

--migrate:down
DROP EXTENSION postgis;
