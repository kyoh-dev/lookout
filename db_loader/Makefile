ENV_FILE ?= .env

.PHONY: build start bash clean format mypy migrate rollback

build:
	@docker-compose build

start:
	@docker-compose -f ../docker-compose.yml up -d db db-loader

bash: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm db-loader bash

clean:
	@docker-compose -f ../docker-compose.yml down --volumes --rmi all

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
