import socket
import threading
import json
import random
import string
from PyQt5.QtCore import pyqtSignal, QThread


class Cliente(QThread):

    senal_recibir_mensaje = pyqtSignal(dict)


    def __init__(self, port, host):
        super().__init__() 
        print('Creando cliente')
        self.port = port
        self.host = host
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.connect_to_server()
            self.listen()
            
        except ConnectionError:
            print('Conexion terminada')
            self.socket_cliente.close()
            self.isConnected = False
            exit()

    def connect_to_server(self):
        self.socket_cliente.connect((self.host, self.port))
        print('Cliente conectado a servidor')


    def listen(self):
        thread = threading.Thread(target=self.listen_thread, daemon=True)
        thread.start()

    def listen_thread(self):
        while True:
            data = self.socket_cliente.recv(2**16)
            decoded_data = data.decode()
            decoded_data = decoded_data.replace('\'', '\"') 
            data = json.loads(decoded_data)
            self.senal_recibir_mensaje.emit(data)
            pass

    def send(self, msg):
        json_msg = json.dumps(msg)
        msg_to_send = json_msg.encode()
        self.socket_cliente.send(msg_to_send)


    def run(self):
        self.online = True



if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook


# if __name__ == '__main__':
#     port = 3245
#     host = 'localhost'
#     client = Cliente(port, host)