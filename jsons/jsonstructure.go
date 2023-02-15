package jsons

type Product struct {
	Name     string `json:"Name"`
	Brand    string `json:"Brand"`
	Price    int    `json:"Price"`
	Category string `json:"Category"`
}

type User struct {
	Username string `json:"Username"`
	Password string `json:"Password"`
	Email    string `json:"Email"`
}

type Transaction struct {
	Products      []Product `json:"Products"`
	BuyerUsername string    `json:"BuyerUsername"`
	Status        string    `json:"Status"`
}
type Login struct {
	Status string `json:"Status"`
}

type Signup struct {
	Status string `json:"Status"`
}
