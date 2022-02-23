package db

import "testing"

func TestServiceConnect(t *testing.T) {
	dbService := Service{}
	if err := dbService.Connect(); err != nil {
		t.Error(err)
	}
}
