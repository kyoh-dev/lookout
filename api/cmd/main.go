package main

import (
	"os"
)

const defaultPort = "8080"

func main() {
	port := os.Getenv("LOOKOUT_API_PORT")
	if port == "" {
		port = defaultPort
	}
}
