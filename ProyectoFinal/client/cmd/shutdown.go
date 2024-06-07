package cmd

import (
	"client/connection"
	"encoding/json"
	"fmt"
	"log"

	"github.com/spf13/cobra"
)

type DataShutdown struct {
	Shutdown bool
	Password string
}

func InitShutdown() *cobra.Command {
	var password string
	var test bool

	var shutdownCmd = &cobra.Command{Use: "shutdown",
		RunE: func(cmd *cobra.Command, args []string) error {

			data := DataShutdown{
				Shutdown: true,
				Password: password,
			}
			if test {
				jsonData, err := json.Marshal(data)
				if err != nil {
					return fmt.Errorf("error marshaling data: %v", err)
				}
				fmt.Fprintln(cmd.OutOrStdout(), string(jsonData))
				return nil
			}
			conn, err := connection.Connect()
			if err != nil {
				return err
			}
			defer conn.Close()

			jsonData, err := json.Marshal(data)
			if err != nil {
				log.Fatalf("Error to convert: %v", err)
			}

			if err := connection.SendData(conn, jsonData); err != nil {
				return err
			}

			response, err := connection.ReceiveData(conn)
			if err != nil {
				return err
			}
			fmt.Println("Server response:", string(response))
			return nil
		},
	}
	shutdownCmd.Flags().StringVarP(&password, "password", "p", "", "Password to shutdown the program")
	shutdownCmd.Flags().BoolVar(&test, "test", false, "print results in terminal")

	return shutdownCmd
}
