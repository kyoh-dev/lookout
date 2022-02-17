package models

import (
	"database/sql"
	"errors"
	"github.com/paulmach/orb/geojson"
)

type recsite struct {
	ID                 int           `json:"id"`
	Name               string        `json:"name"`
	Latitude           float64       `json:"latitude"`
	Longitude          float64       `json:"longitude"`
	DisabledAccess     string        `json:"disabledAccess"`
	AccessDescr        string        `json:"accessDescr"`
	Fee                int           `json:"fee"`
	Comments           string        `json:"comments"`
	MaintainedBy       string        `json:"maintainedBy"`
	ClosedStatus       string        `json:"closedStatus"`
	ClosedOn           string        `json:"closedOn"`
	ReopenOn           string        `json:"reopenOn"`
	ClosedReason       string        `json:"closedReason"`
	Camping            bool          `json:"camping"`
	CampingDescr       string        `json:"campingDescr"`
	Campervanning      bool          `json:"campervanning"`
	CampervanningDescr string        `json:"campervanningDescr"`
	CampervanType      string        `json:"campervanType"`
	TrailBikeArea      bool          `json:"trailBikeArea"`
	TrailBikeAreaDescr string        `json:"trailBikeAreaDescr"`
	Heritage           bool          `json:"heritage"`
	HeritageDescr      string        `json:"heritageDescr"`
	Fishing            bool          `json:"fishing"`
	FishingDescr       string        `json:"fishingDescr"`
	Fossicking         bool          `json:"fossicking"`
	FossickingDescr    string        `json:"fossickingDescr"`
	HangGliding        bool          `json:"hangGliding"`
	HangGlidingDescr   string        `json:"hangGlidingDescr"`
	HorseRiding        bool          `json:"horseRiding"`
	HorseRidingDescr   string        `json:"horseRidingDescr"`
	Paddling           bool          `json:"paddling"`
	PaddlingDescr      string        `json:"paddlingDescr"`
	Picnicing          bool          `json:"picnicing"`
	PicnicingDescr     string        `json:"picnicingDescr"`
	NoiseWarning       bool          `json:"noiseWarning"`
	NoiseWarningDescr  string        `json:"noiseWarningDescr"`
	RockClimbing       bool          `json:"rockClimbing"`
	RockClimbingDescr  string        `json:"rockClimbingDescr"`
	DogWalking         bool          `json:"dogWalking"`
	DogWalkingDescr    string        `json:"dogWalkingDescr"`
	Wildlife           bool          `json:"wildlife"`
	WildlifeDescr      string        `json:"wildlifeDescr"`
	NumBbqElectric     int           `json:"numBbqElectric"`
	NumBbqPit          int           `json:"numBbqPit"`
	NumBbqGas          int           `json:"numBbqGas"`
	NumBbqWood         int           `json:"numBbqWood"`
	RepPoint           geojson.Point `json:"repPoint"`
}

func (r *recsite) getRecSite(db *sql.DB) error {
	return errors.New("not implemented")
}

func getRecSites(db *sql.DB, start, count int) ([]recsite, error) {
	return nil, errors.New("not implemented")
}
