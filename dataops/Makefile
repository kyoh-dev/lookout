.PHONY: setup format mypy bash migrate rollback

setup:
	@test -d .venv || python3 -m venv .venv

format: setup
	@python -m black .

mypy: setup
	@python -m mypy .

bash:
	@docker-compose -f ../docker-compose.yml run --rm dataops

migrate:
	@docker-compose -f ../docker-compose.yml run --rm dataops dbmate -d "./migrations" up

rollback:
	@docker-compose -f ../docker-compose.yml run --rm dataops dbmate -d "./migrations" down
