ENV_FILE ?= .env

.PHONY: build start clean format mypy migrate

build:
	@docker-compose build

start:
	@docker-compose up -d

clean:
	@docker-compose down --volumes --rmi all

format:
	@black ./db/

mypy:
	@mypy ./db/

migrate: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL up

rollback: $(ENV_FILE)
	@dbmate -e TEST_DATABASE_URL down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
