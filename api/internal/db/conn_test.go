package db

import "testing"

func TestServiceConnect(t *testing.T) {
	dbPool := Pool{}
	if err := dbPool.Connect(); err != nil {
		t.Error(err)
	}
}
