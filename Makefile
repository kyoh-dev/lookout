.PHONY: build start clean

build:
	@docker-compose build

start:
	@docker-compose up -d

clean:
	@docker-compose down --volumes --rmi all
