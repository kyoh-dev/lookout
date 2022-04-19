-- migrate:up
CREATE SCHEMA raw;

-- migrate:down
DROP SCHEMA raw CASCADE;
