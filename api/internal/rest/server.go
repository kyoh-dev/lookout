package rest

import (
	"github.com/kyoh-dev/lookout/internal/db"
	"github.com/labstack/echo/v4"
)

type Service struct {
	HTTPService *echo.Echo
	DBConn *db.Pool
}
