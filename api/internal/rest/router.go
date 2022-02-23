package rest

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func Setup(r *echo.Echo) {
	r.Use(middleware.Logger())
	r.Use(middleware.Recover())

	r.GET("/health", func(c echo.Context) error {
		return c.String(http.StatusOK, "OK")
	})
}
