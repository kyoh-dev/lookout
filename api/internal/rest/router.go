package rest

import (
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func Setup(r *echo.Echo) {
	r.Use(middleware.Logger())
	r.Use(middleware.Recover())

	r.GET("/health", healthCheck)
}
