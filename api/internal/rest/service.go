package rest

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/gorilla/mux"
	"github.com/jackc/pgx/v4/pgxpool"
)

const (
	minConnections  = 1
	maxConnections  = 20
	idleConnTimeout = 30 // seconds
)

type Service struct {
	Router *mux.Router
	DBConn *pgxpool.Pool
}

func (s *Service) ConnectDB(connectionString string) {
	poolConfig, err := pgxpool.ParseConfig(connectionString)
	if err != nil {
		fmt.Fprintf(os.Stderr, "unable to parse db connection string: %v\n", err)
		os.Exit(1)
	}

	poolConfig.MinConns = minConnections
	poolConfig.MaxConns = maxConnections
	poolConfig.MaxConnIdleTime = idleConnTimeout * time.Second

	conn, err := pgxpool.ConnectConfig(context.Background(), poolConfig)
	if err != nil {
		fmt.Fprintf(os.Stderr, "db connection failed: %v\n", err)
		os.Exit(1)
	}

	s.DBConn = conn
}

func (s *Service) Start(addr string) {}
