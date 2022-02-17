package main

import (
	"os"

	"github.com/kyoh-dev/lookout/internal/rest"
)

func main() {
	srv := rest.Server{}
	srv.Initialise(
		os.Getenv("DB_USER"),
		os.Getenv("DB_PASSWORD"),
		os.Getenv("DB_NAME"))

	srv.Run(":8010")
}
