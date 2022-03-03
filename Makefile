ENV_FILE ?= .env

.PHONY: build start clean bash format mypy migrate rollback

venv:
	@test -d .venv || python3 -m venv .venv

build:
	@docker-compose build

start:
	@docker-compose up -d

clean:
	@docker-compose down --volumes --rmi all

bash: $(ENV_FILE)
	@docker-compose run --rm app bash

format: venv
	@python -m black .

mypy: venv
	@python -m mypy .

migrate: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL -d "./data/migrations" up

rollback: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL -d "./data/migrations" down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
