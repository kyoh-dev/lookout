.PHONY: start clean pytype-check

start:
	@docker-compose -f docker-compose.dev.yml up

clean:
	@docker-compose -f docker-compose.dev.yml down --volumes --rmi all

pytype-check:
	@pytype ./data
