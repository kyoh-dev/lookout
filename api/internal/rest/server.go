package rest

import (
	"database/sql"

	"github.com/gorilla/mux"
	_ "github.com/lib/pq"
)

type Server struct {
	Router *mux.Router
	DB     *sql.DB
}

func (a *Server) Initialise(user, password, dbname string) {}
func (a *Server) Run(addr string)                          {}
