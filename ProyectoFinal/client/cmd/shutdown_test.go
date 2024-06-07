package cmd

import (
	"encoding/json"
	"strings"
	"testing"
)

func TestShutdownCmd(t *testing.T) {
	tests := []struct {
		args         []string
		expectedData DataShutdown
	}{
		{
			args: []string{"--password", "messi", "--test"},
			expectedData: DataShutdown{
				Shutdown: true,
				Password: "messi",
			},
		},
		{
			args: []string{"--password", "armando", "--test"},
			expectedData: DataShutdown{
				Shutdown: true,
				Password: "armando",
			},
		},
	}

	for _, tt := range tests {
		t.Run(strings.Join(tt.args, " "), func(t *testing.T) {

			output, err := mockExecuteCommand(t, InitShutdown(), tt.args)
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}

			var outputData DataShutdown
			if err := json.Unmarshal([]byte(output), &outputData); err != nil {
				t.Fatalf("error unmarshaling output data: %v", err)
			}

			if outputData != tt.expectedData {
				t.Errorf("expected %+v, got %+v", tt.expectedData, outputData)
			}
		})
	}
}
