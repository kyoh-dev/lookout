-- migrate:up
CREATE SCHEMA staging;

-- migrate:down
DROP SCHEMA staging CASCADE;
