package models

import (
	"context"
	"errors"

	"github.com/kyoh-dev/lookout/internal/db"
	"github.com/paulmach/orb/geojson"
)

type recsite struct {
	ID                 int           `param:"id" json:"id"`
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
	VersionDate        string        `json:"versionDate"`
	RepPoint           geojson.Point `json:"repPoint"`
}

func (r *recsite) getRecSite(db *db.Pool) error {
	query := `
	SELECT
	  name,
	  latitude,
	  longitude,
	  disabed_access,
	  access_descr,
	  fee,
	  comments,
	  maintained_by,
	  closed_status,
	  closed_descr,
	  closed_on,
	  reopen_on,
	  camping,
	  camping_descr,
	  campervanning,
	  campervanning_descr,
	  campervan_type,
	  trail_bike_area,
	  trail_bike_area_descr,
	  heritage,
	  heritage_descr,
	  fishing,
	  fishing_descr,
	  fossicking,
	  fossicking_descr,
	  hang_gliding,
	  hang_gliding_descr,
	  horse_riding,
	  horse_riding_descr,
	  paddling,
	  paddling_descr,
	  picnicing,
	  picnicing_descr,
	  noise_warning,
	  noise_warning_descr,
	  rock_climbing,
	  rock_climbing_descr,
	  dog_walking,
	  dog_walking_descr,
	  wildlife,
	  wildlife_descr,
	  num_bbq_electric,
	  num_bbq_pit,
	  num_bbq_gas,
	  num_bbq_wood,
	  version_date,
	  rep_point
	FROM public.rec_site
	WHERE id = $1;
	`

	return db.Conn.QueryRow(context.Background(), query, r.ID).Scan(
		&r.Name, &r.Latitude, &r.Longitude, &r.DisabledAccess,
		&r.AccessDescr, &r.Fee, &r.Comments, &r.MaintainedBy,
		&r.ClosedStatus, &r.ClosedOn, &r.ReopenOn, &r.ClosedReason,
		&r.Camping, &r.CampingDescr, &r.Campervanning, &r.CampervanningDescr,
		&r.CampervanType, &r.TrailBikeArea, &r.TrailBikeAreaDescr,
		&r.Heritage, &r.HeritageDescr, &r.Fishing, &r.FishingDescr,
		&r.Fossicking, r.FossickingDescr, &r.HangGliding, &r.HangGlidingDescr,
		&r.HorseRiding, &r.HorseRidingDescr, &r.Paddling, &r.PaddlingDescr,
		&r.Picnicing, &r.PicnicingDescr, &r.NoiseWarning, &r.NoiseWarningDescr,
		&r.RockClimbing, &r.RockClimbingDescr, &r.DogWalking, &r.DogWalkingDescr,
		&r.Wildlife, &r.WildlifeDescr, &r.NumBbqElectric, &r.NumBbqPit,
		&r.NumBbqGas, r.NumBbqWood, &r.VersionDate, &r.RepPoint)
}

func getRecSites(db *db.Pool, start, count int) ([]recsite, error) {
	return nil, errors.New("not implemented")
}
