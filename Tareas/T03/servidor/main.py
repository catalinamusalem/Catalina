import socket 
import threading
import json
import time
import random


class Servidor:


    def __init__(self, port, host):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        self.juego_en_curso = False
        self.usuarios = []
        self.bind_listen()
        self.accept_connections()
        self.online()
        
        
        
    
    def bind_listen(self):
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(4)
        print(f'Servidor escuchando en {self.host} : {self.port}')

    def accept_connections(self):
        thread = threading.Thread( \
            target=self.accept_connections_thread, \
            daemon=True)
        thread.start()
    
    def accept_connections_thread(self):

        while True:
            client_socket, address = self.socket_server.accept()
            self.sockets[client_socket] = address
            listening_client_thread = threading.Thread( \
                target=self.listen_client_thread, \
                args=(client_socket, ), \
                daemon=True)
            listening_client_thread.start()

    def listen_client_thread(self, client_socket):
        
        while True:
            response = client_socket.recv(2**16)
            recived = response.decode()
            recived = json.loads(recived)
            self.chat_management(recived, client_socket)


    def online(self):
        while True:
            pass


    def chat_management(self, msg, client_socket):
        print(msg)
        if msg["tipo"] == "nombre":
            if self.juego_en_curso == False:
                if len(self.usuarios) < 4: #arreglar segun parametro json
                    if msg["msg"].isalnum() == True and " " not in msg :
                        if msg["msg"] in self.usuarios:
                            msg_to_send = {'type': 'verificacion usuario', 'estado': "False"}
                        else:
                            msg_to_send = {'type': 'verificacion usuario', 'estado': "True"}
                            print(self.usuarios)
                            self.usuarios.append(msg["msg"])
                            self.sockets[client_socket] = msg
                    else:
                        msg_to_send = {'type': 'verificacion usuario', 'estado': "No cumple requisitos"}
                else:
                    msg_to_send = {'type': 'verificacion usuario', 'estado': "Partida completa"}
            else:
                msg_to_send = {'type': 'verificacion usuario', 'estado': "Partida en progreso"}
        self.send(msg_to_send, client_socket)

        #for skt in self.sockets.keys():
        #    self.send(msg_to_send, skt)

    
    def send(self, value, sock):
        str_value = str(value)
        print(str_value)
        msg_bytes = str_value.encode()
        sock.send(msg_bytes)

#-----------------------------------------------------------------------------------

if __name__ == '__main__':
    port = 3245
    host = 'localhost'
    server = Servidor(port, host)
