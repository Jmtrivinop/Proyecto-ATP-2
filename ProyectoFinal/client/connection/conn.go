package connection

import (
	"bytes"
	"fmt"
	"net"
)

func Connect() (net.Conn, error) {
	conn, err := net.Dial("tcp", "localhost:65092")
	if err != nil {
		return nil, fmt.Errorf("Error connecting to server: %v", err)
	}
	return conn, nil
}

func SendData(conn net.Conn, jsonData []byte) error {
	_, err := conn.Write(jsonData)
	if err != nil {
		return fmt.Errorf("Error sending data: %v", err)
	}
	return nil
}

func ReceiveData(conn net.Conn) ([]byte, error) {
	buffer := make([]byte, 1024)
	var data []byte

	for {

		bytesRead, err := conn.Read(buffer)
		if err != nil {

			return nil, fmt.Errorf("Error reading data: %v", err)
		}
		data = append(data, buffer[:bytesRead]...)

		if bytes.Contains(buffer[:bytesRead], []byte{'\n'}) {
			break
		}
	}

	return data, nil
}
