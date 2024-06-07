import os
import signal
from flask import Flask, request, jsonify
from generate_numbers.generate_normal import GenerateNormal
from generate_numbers.generate_uniform import GenerateUniform
from my_app import MyApp
from encrypt import EncryptionHandler
import random

app = Flask(__name__)
encryption_handler = EncryptionHandler()
encryption_handler.generate_keys()
client_public_key = None

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return jsonify({"message": "Shutdown the program"})

def shutdown_server():
    
    pid = os.getpid()
    
    os.kill(pid, signal.SIGINT)

@app.route('/numbers', methods=['POST'])
def get_numbers():
    try:
        my_app = MyApp()
        data = request.json
        decrypted_data = encryption_handler.decrypt(data)
        range = decrypted_data['AmountData']
        min = decrypted_data['Minimum']
        max = decrypted_data['Maximum']
        flag = random.choice([True, False])

        if flag:
                
                result = my_app.run(GenerateNormal(), min, max, range,decrypted_data['Test'])
                
        else:
                result = my_app.run(GenerateUniform(), min, max, range, decrypted_data['Test']) 
                
        
        encrypted_result = encryption_handler.encrypt(result, client_public_key)
    except Exception as e:
        
                                    
        encrypted_result = [f'Error: {e}']

    return jsonify(encrypted_result)

@app.route('/public_key', methods=['POST'])
def receive_public_key():
    global client_public_key
    data = request.get_json()
   
    client_public_key = data['public_key']
    

    return jsonify({"public_key": encryption_handler.public_key.export_key().decode()})


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
