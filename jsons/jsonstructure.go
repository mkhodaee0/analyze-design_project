package jsons

import "github.com/google/uuid"

type Product struct {
	ID       uuid.UUID `json:"ID"`
	Name     string    `json:"Name"`
	Brand    string    `json:"Brand"`
	Price    int       `json:"Price"`
	Category string    `json:"Category"`
}

type User struct {
	ID       uuid.UUID `json:"ID"`
	Username string    `json:"Username"`
	Password string    `json:"Password"`
}

type Transaction struct {
	Products []Product `json:"Products"`
	BuyerID  uuid.UUID `json:"ID"`
	Status   string    `json:"Status"`
}
