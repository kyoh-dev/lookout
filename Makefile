.PHONY: setup build start clean format mypy

setup: $(ENV_FILE)
	@test -d .venv || python3 -m venv .venv

build:
	@docker-compose build

start:
	@docker-compose up -d

clean:
	@docker-compose down --volumes --rmi all

format: setup
	@python -m black .

mypy: setup
	@python -m mypy .
