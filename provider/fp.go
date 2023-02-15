package provider

import (
	"github.com/gofiber/fiber/v2"
	"github.com/mkhodaee0/analyze-design_project/jsons"
	"github.com/mkhodaee0/analyze-design_project/todb"
)

func loginhandler(c *fiber.Ctx) error {
	j := &jsons.User{}
	err := c.BodyParser(j)
	if err != nil {
		panic(err)
	}

	return c.SendStatus(Isvalid(*j))
}

func signuphandler(c *fiber.Ctx) error {
	j := &jsons.User{}
	s := &jsons.Signup{}
	err := c.BodyParser(j)
	if err != nil {
		panic(err)
	}
	todb.Poster(j, s, "signup")
	if s.Status == "added successfully" {
		return c.SendStatus(600)
	} else {
		return c.SendStatus(601)
	}
}
func Provide() {
	app := fiber.New()

	app.Post("/api/login", loginhandler)
	app.Post("/api/signup", signuphandler)

	app.Listen(":8001")
}
