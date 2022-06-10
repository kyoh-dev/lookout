ENV_FILE	?=	.env

.PHONY: bash migrate rollback

bash: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm dataops

migrate: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm dataops dbmate -d "./migrations" up

rollback: $(ENV_FILE)
	@docker-compose -f ../docker-compose.yml run --rm dataops dbmate -d "./migrations" down

$(ENV_FILE):
	@cp -v $(ENV_FILE).example $(ENV_FILE)
