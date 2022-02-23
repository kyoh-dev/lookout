package models

import (
	"context"
	"errors"

	"github.com/kyoh-dev/lookout/internal/db"
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
	VersionDate     string               `json:"versionDate"`
	Geometry        geojson.MultiPolygon `json:"geometry"`
}

func (p *park) getPark(db *db.Service) error {
	query := `
	SELECT 
	  name,
	  type, 
	  area_sqm, 
	  hectares,
	  managed_by, 
	  iucn_code,
	  established_date,
	  version_date,
	  ST_GeomAsGeoJSON(geometry) 
	FROM public.park 
	WHERE id = $1;
	`
	return db.Conn.QueryRow(context.Background(), query, p.ID).Scan(
		&p.Name, &p.Type, &p.AreaSqm, &p.Hectares,
		&p.ManagedBy, &p.IucnCode, &p.EstablishedDate,
		&p.VersionDate, &p.Geometry)
}

func getParks(db *db.Service) ([]park, error) {
	return nil, errors.New("not implemented")
}
