package models

import "github.com/paulmach/orb/geojson"

type Park struct {
	ID int `json:"id"`
	Name string `json:"name"`
	Type string `json:"type"`
	AreaSqm float64 `json:"areaSqm"`
	Hectares float64 `json:"hectares"`
	ManagedBy string `json:"managedBy"`
	IucnCode string `json:"iucnCode"`
	EstablishedDate string `json:"establishedDate"`
	Geometry geojson.MultiPolygon `json:"geometry"`
}
