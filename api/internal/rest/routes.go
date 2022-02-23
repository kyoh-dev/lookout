package rest

import (
	"github.com/kyoh-dev/lookout/internal/models"
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
)

func healthCheck(c echo.Context) error {
	return c.String(http.StatusOK, "OK")
}

func (s *Service) getPark(c echo.Context) error {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		return c.JSON(http.StatusNotFound, map[string]string {
			"error": "Invalid ID provided",
		})
	}

	p := models.Park{ID: id}
	if err := p.GetPark(s.DBConn); err != nil {
		return c.JSON(http.StatusNotFound, map[string]string {
			"error": "Park cannot be found",
		})
	}

	return c.JSON(http.StatusOK, p)
}
