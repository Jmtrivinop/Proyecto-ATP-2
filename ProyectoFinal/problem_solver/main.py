import logging
import socket
import json
import requests
from my_app import MyApp
from encrypt import EncryptionHandler
from auth import Auth
from file.file import File



class Main:
    def __init__(self):
        logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
        try:
            self.encryption_handler = EncryptionHandler()
            self.encryption_handler.generate_keys()
        except Exception as e:
            logging.error(f"Error initializing EncryptionHandler: {e}")
            raise

    def start_server(self, host, port):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen()
            logging.info(f'Server started on {host}:{port}')
            
        except socket.error as e:
            logging.error(f"Socket error: {e}")
            return
        try:
            public_key_message = {"public_key": self.encryption_handler.public_key.export_key().decode()}
            public = requests.post('http://localhost:5000/public_key', json=public_key_message)
            client_public_key = public.json()
        except Exception:
             result = {"message": "Can not find the server flask"}
        my_app = MyApp()
        flag = True
        
        while flag:
            try:
                conn, _ = server.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break

                        try:
                            dataJson = json.loads(data.decode('utf-8'))
                        except json.JSONDecodeError as e:
                            logging.error(f"JSON decode error: {e}")
                            conn.sendall((json.dumps({"message": "Invalid JSON format"})+  '\n').encode())
                            continue

                        if 'Shutdown' in dataJson:
                            
                            try:
                                password_file = File.read_file()
                                password = dataJson['Password']
                                confirm_password = Auth.compare_password(password_file, password)
                                
                                if dataJson['Shutdown'] and confirm_password:
                                    
                                    requests.get('http://localhost:5000/shutdown')
                                    
                                else:
                                    result = {"message": "The password is incorrect"}
                            

                            except requests.exceptions.ConnectionError:
                                logging.info('Shutting down the program')
                                flag = False
                                result = {"message": "Shutdown the program"}
                            except Exception:
                                result = {"message": "Can not find flask"}
                        else:
                            try:
                                
                                dataJson_encrypted = self.encryption_handler.encrypt(dataJson, client_public_key['public_key'])
                                get_numbers = requests.post('http://localhost:5000/numbers', json=dataJson_encrypted)
                                number_list = get_numbers.json()
                                
                                decrypted_data = self.encryption_handler.decrypt(number_list)
                                
                                problem = my_app.select_problem(dataJson['Problem'])

                                if problem == None:
                                    
                                  result = {"message": ["That is not a problem"]}
                                else:
                                    logging.info(f'Processed problem {dataJson["Problem"]}, range: {dataJson["AmountData"]}, min:{dataJson["Minimum"]}, max: {dataJson["Maximum"]}')
                                    resultJson = my_app.run(problem, decrypted_data)
                                    result = {"Results: ": resultJson}
                                    
                            except Exception as e:
                                logging.error(f"Error processing data: {e}")
                                result = {"message": ["Error processing data"]}

                        conn.sendall((json.dumps(result) + '\n').encode())
            except Exception as e:
                logging.error(f"Connection error: {e}")

if __name__ == "__main__":
    server = Main()
    server.start_server('localhost', 65092)
