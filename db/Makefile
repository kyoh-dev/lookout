ENV_FILE ?= .env

.PHONY: bash format mypy migrate rollback

bash: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm db-loader bash

format:
	@black ./

mypy:
	@mypy ./

migrate: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL up

rollback: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
