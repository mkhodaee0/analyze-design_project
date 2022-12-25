package provider

import "github.com/gofiber/fiber/v2"

func handler(c *fiber.Ctx) error {
	return c.SendString("Hello, World!")
}

func Provide() {
	app := fiber.New()

	app.Get("/", handler)

	app.Listen(":8001")
}
