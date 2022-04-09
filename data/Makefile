ENV_FILE	?=	.envrc

.PHONY: setup format mypy bash migrate rollback

setup: $(ENV_FILE)
	@test -d .venv || python3 -m venv .venv

format: setup
	@python -m black .

mypy: setup
	@python -m mypy .

bash:
	@docker-compose -f ../docker-compose.yml run --rm data bash

migrate:
	@docker-compose -f ../docker-compose.yml run --rm data dbmate -d "./migrations" up

rollback:
	@docker-compose -f ../docker-compose.yml run --rm data dbmate -d "./migrations" down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
