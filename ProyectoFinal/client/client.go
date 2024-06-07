package main

import (
	"client/cmd"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use: "app",
}

func main() {
	rootCmd.AddCommand(cmd.InitClient())
	rootCmd.AddCommand(cmd.InitShutdown())

	rootCmd.Execute()
}
