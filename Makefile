ENV_FILE	?=	.envrc

.PHONY: build start clean bash format mypy migrate rollback

setup: $(ENV_FILE)
	@test -d .venv || python3 -m venv .venv

build:
	@docker-compose build

start:
	@docker-compose up -d

clean:
	@docker-compose down --volumes --rmi all

bash:
	@docker-compose run --rm data bash

format: setup
	@python -m black .

mypy: setup
	@python -m mypy .

migrate:
	@docker-compose run --rm data dbmate -d "./migrations" up

rollback:
	@@docker-compose run --rm data dbmate -d "./migrations" down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
