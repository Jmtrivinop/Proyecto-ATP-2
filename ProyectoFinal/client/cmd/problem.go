package cmd

import (
	"client/connection"
	"client/file"
	"encoding/json"
	"fmt"
	"log"

	"github.com/spf13/cobra"
)

type DataClient struct {
	Problem    string
	AmountData int64
	Minimum    int64
	Maximum    int64
	Test       bool
}

func InitClient() *cobra.Command {
	var problem string
	var amountData int64
	var minimum int64
	var maximum int64
	var output string
	var print string
	var test bool

	var clientCmd = &cobra.Command{Use: "problem",
		RunE: func(cmd *cobra.Command, args []string) error {
			data := DataClient{
				Problem:    problem,
				AmountData: amountData,
				Minimum:    minimum,
				Maximum:    maximum,
				Test:       test,
			}

			if test {
				jsonData, err := json.Marshal(data)
				if err != nil {
					return fmt.Errorf("error marshaling data: %v", err)
				}
				fmt.Fprintln(cmd.OutOrStdout(), string(jsonData))
				//return nil
			}

			jsonData, err := json.Marshal(data)
			if err != nil {
				log.Fatalf("Error to convert: %v", err)
			}

			conn, err := connection.Connect()
			if err != nil {
				return err
			}
			defer conn.Close()

			if err := connection.SendData(conn, jsonData); err != nil {
				return err
			}

			response, err := connection.ReceiveData(conn)
			if err != nil {
				return err
			}
			if print == "yes" {
				var result map[string][]string
				err := json.Unmarshal(response, &result)
				if err != nil {
					return fmt.Errorf("error unmarshaling response: %v", err)
				}

				for key, values := range result {
					fmt.Printf("%s\n", key)
					for _, value := range values {
						fmt.Printf("  %s\n", value)
					}
				}
			} else {
				fmt.Println("Good bye")
			}

			if output != "" {
				err := file.WriteToFile(output, response)
				if err != nil {

					return err
				}
			}

			return nil
		},
	}
	clientCmd.Flags().StringVarP(&problem, "problem", "p", "fibonacci", "Problem to resolv")
	clientCmd.Flags().Int64VarP(&amountData, "amount", "a", 40, "amount of data")
	clientCmd.Flags().Int64VarP(&minimum, "minimum", "m", 0, "minimum number")
	clientCmd.Flags().Int64VarP(&maximum, "maximum", "t", 100, "maximum number")
	clientCmd.Flags().StringVarP(&output, "output", "o", "", "name of output file")
	clientCmd.Flags().StringVarP(&print, "print", "P", "yes", "print results in terminal")
	clientCmd.Flags().BoolVar(&test, "test", false, "print results in terminal")

	return clientCmd

}
