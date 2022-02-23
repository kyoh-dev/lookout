ENV_FILE ?= .env

.PHONY: bash format mypy migrate rollback

install:
	( \
	   source .venv/bin/activate; \
	   pip install -r requirements.txt; \
	)

bash: $(ENV_FILE)
	@docker-compose run --rm db-loader bash

format: venv
	@python -m black .

mypy: venv
	@python -m mypy .

migrate: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL -d "./migrations" up

rollback: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL -d "./migrations" down

venv:
	@test -d .venv || python3 -m venv .venv

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
