ENV_FILE ?= .env

.PHONY: build start bash clean format mypy migrate rollback

build:
	@docker-compose build

start:
	@docker-compose up -d db db-loader

bash: $(ENV_FILE)
	@docker-compose run --rm db-loader bash

clean:
	@docker-compose down --volumes --rmi all

test:
	@docker-compose build db-loader
	@docker-compose up --build --abort-on-container-exit --exit-code-from db-loader-test db-test db-loader-test

format:
	@black ./db_loader/

mypy:
	@mypy ./db_loader/

migrate: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL up

rollback: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
