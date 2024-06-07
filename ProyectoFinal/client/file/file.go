package file

import (
	"encoding/json"
	"fmt"
	"os"
)

func WriteToFile(filename string, data []byte) error {
	var result map[string][]string
	err := json.Unmarshal(data, &result)
	if err != nil {
		return fmt.Errorf("error unmarshaling response: %v", err)
	}

	file, err := os.Create(filename + ".txt")
	if err != nil {
		return fmt.Errorf("error creating file: %v", err)
	}
	defer file.Close()

	for _, values := range result {
		for _, value := range values {
			_, err := file.WriteString(fmt.Sprintf("%s\n", value))
			if err != nil {
				return fmt.Errorf("error writing to file: %v", err)
			}
		}
	}
	return nil
}
