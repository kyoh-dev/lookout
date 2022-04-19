ENV_FILE	?=	.env

.PHONY: setup format mypy bash migrate rollback

setup: $(ENV_FILE)
	@test -d .venv || python3 -m venv .venv

format: setup
	@python -m black .

mypy: setup
	@python -m mypy .

bash: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm dataops

migrate: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm dataops dbmate -d "./migrations" up

rollback: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm dataops dbmate -d "./migrations" down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
