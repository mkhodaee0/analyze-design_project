package consume

import (
	"encoding/json"
	"log"
	"net/http"
	"time"
)

var url string = "localhost:8000"
var client *http.Client

func errorHandler(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

// target must be a pointer
func Getter(target interface{}, dir string) error {
	client = &http.Client{Timeout: 10 * time.Second}

	resp, err := client.Get(url + dir)
	errorHandler(err)

	errorHandler(json.NewDecoder(resp.Body).Decode(target))

	return nil
}
