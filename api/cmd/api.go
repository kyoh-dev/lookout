package main

import (
	"os"

	"github.com/kyoh-dev/lookout/internal/rest"
)

const defaultPort = "8080"

func main() {
	srv := rest.Service{}
	srv.ConnectDB(os.Getenv("DATABASE_URL"))

	port := os.Getenv("API_PORT")
	if port == "" {
		port = defaultPort
	}

	srv.Start(":" + port)
}
