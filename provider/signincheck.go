package provider

import (
	"github.com/mkhodaee0/analyze-design_project/jsons"
	"github.com/mkhodaee0/analyze-design_project/todb"
)

func Isvalid(j jsons.User) int {
	l := &jsons.Login{}
	todb.Poster(&j, l, "login")
	if l.Status == "correct" {
		return 600
	} else if l.Status == "account exists" {
		return 601
	} else {
		return 602
	}
}
