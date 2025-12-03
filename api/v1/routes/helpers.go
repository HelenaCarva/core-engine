package helpers

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"strings"
)

func parseJSONBody(w http.ResponseWriter, r *http.Request, target interface{}) error {
	if r.Header.Get("Content-Type") != "application/json" {
		http.Error(w, "expected application/json content type", http.StatusBadRequest)
		return errors.New("invalid content type")
	}

	decoder := json.NewDecoder(r.Body)
	decoder.DisallowUnknownFields()
	if err := decoder.Decode(target); err != nil {
		http.Error(w, fmt.Sprintf("invalid json body: %v", err), http.StatusBadRequest)
		return err
	}
	return nil
}

func checkAPIKey(r *http.Request) (string, error) {
	apiKey := r.Header.Get("X-API-KEY")
	if apiKey == "" {
		return "", errors.New("missing api key")
	}
	return apiKey, nil
}

func logRequest(r *http.Request) {
	log.Printf("%s %s", r.Method, r.URL)
}

func writeJSONResponse(w http.ResponseWriter, data interface{}, code int) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)
	if err := json.NewEncoder(w).Encode(data); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func parseQueryString(r *http.Request, key string) (string, error) {
	values := r.URL.Query()
	value := values.Get(key)
	if value == "" {
		return "", errors.New("missing query parameter")
	}
	return value, nil
}

func validateString(s string) error {
	if strings.TrimSpace(s) == "" {
		return errors.New("empty string")
	}
	return nil
}