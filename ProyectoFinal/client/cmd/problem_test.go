package cmd

import (
	"bytes"
	"encoding/json"
	"strings"
	"testing"

	"github.com/spf13/cobra"
)

func mockExecuteCommand(t *testing.T, cmd *cobra.Command, args []string) (string, error) {
	t.Helper()
	buf := new(bytes.Buffer)
	cmd.SetOut(buf)
	cmd.SetErr(buf)
	cmd.SetArgs(args)

	err := cmd.Execute()
	return buf.String(), err
}

func TestClientCmd(t *testing.T) {
	tests := []struct {
		args         []string
		expectedData DataClient
	}{
		{
			args: []string{"--problem", "Sum", "--amount", "500", "--minimum", "1", "--maximum", "1000", "--test"},
			expectedData: DataClient{
				Problem:    "Sum",
				AmountData: 500,
				Minimum:    1,
				Maximum:    1000,
				Test:       true,
			},
		},
		{
			args: []string{"--problem", "Factorial", "--amount", "100", "--minimum", "0", "--maximum", "10", "--test"},
			expectedData: DataClient{
				Problem:    "Factorial",
				AmountData: 100,
				Minimum:    0,
				Maximum:    10,
				Test:       true,
			},
		},
	}

	for _, tt := range tests {
		t.Run(strings.Join(tt.args, " "), func(t *testing.T) {

			output, err := mockExecuteCommand(t, InitClient(), tt.args)
			if err != nil {
				t.Fatalf("unexpected error: %v", err)
			}

			var outputData DataClient
			if err := json.Unmarshal([]byte(output), &outputData); err != nil {
				t.Fatalf("error unmarshaling output data: %v", err)
			}

			if outputData != tt.expectedData {
				t.Errorf("expected %+v, got %+v", tt.expectedData, outputData)
			}
		})
	}
}
