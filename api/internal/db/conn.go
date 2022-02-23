package db

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/jackc/pgx/v4/pgxpool"
)

const (
	minConnections  = 1
	maxConnections  = 15
	maxConnIdleTime = 30 // seconds
)

type Pool struct {
	Conn *pgxpool.Pool
}

func (s *Pool) Connect() error {
	poolConfig, err := pgxpool.ParseConfig(os.Getenv("DATABASE_URL"))
	if err != nil {
		return fmt.Errorf("unable to parse database connection string: %w", err)
	}

	poolConfig.MinConns = minConnections
	poolConfig.MaxConns = maxConnections
	poolConfig.MaxConnIdleTime = maxConnIdleTime * time.Second

	conn, err := pgxpool.ConnectConfig(context.Background(), poolConfig)
	if err != nil {
		return fmt.Errorf("database connection failed: %w", err)
	}

	s.Conn = conn

	return nil
}
