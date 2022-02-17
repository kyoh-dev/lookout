package models

import (
	"database/sql"
	"errors"
	"github.com/paulmach/orb/geojson"
)

type park struct {
	ID              int                  `json:"id"`
	Name            string               `json:"name"`
	Type            string               `json:"type"`
	AreaSqm         float64              `json:"areaSqm"`
	Hectares        float64              `json:"hectares"`
	ManagedBy       string               `json:"managedBy"`
	IucnCode        string               `json:"iucnCode"`
	EstablishedDate string               `json:"establishedDate"`
	Geometry        geojson.MultiPolygon `json:"geometry"`
}

func (p *park) getPark(db *sql.DB) error {
	return errors.New("not implemented")
}

func getParks(db *sql.DB, start, count int) ([]park, error) {
	return nil, errors.New("not implemented")
}
