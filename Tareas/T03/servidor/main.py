import socket 
import threading
import json
import time
import random
from generador_de_mazos import sacar_cartas
import base64 



with open("parametros.json") as f:
    data = json.load(f)

class Servidor:


    def __init__(self, port, host):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sockets = {}
        self.juego_en_curso = False
        self.usuarios = []
        self.cartas_acumuladas = 0
        self.gritar_dcc4 = False
        self.turno_jugador = " "
        self.color = ""
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
            self.sockets[client_socket] = {"address": address, "jugando": False}
            listening_client_thread = threading.Thread( \
                target=self.listen_client_thread, \
                args=(client_socket, ), \
                daemon=True)
            listening_client_thread.start()

    def listen_client_thread(self, client_socket):
        a = (self.sockets[client_socket]["address"])
        print( "| Cliente            | Evento            | Detalles           | ")
        print(f"|{a}| conectado         | Esperando nombre ..| ")
        while True:
            response = client_socket.recv(2**16)
            recived = response.decode()
            recived = json.loads(recived)
            self.recibir_mensaje(recived, client_socket)
    def online(self):
        while True:
            pass


    def recibir_mensaje(self, msg, client_socket):
        a = (self.sockets[client_socket]["address"])
        b = msg["msg"]
        if msg["tipo"] == "nombre":
            if self.juego_en_curso == False:
                if len(self.usuarios) < data["cantidad_jugadores_partida"]: 
                    if msg["msg"].isalnum() == True and " " not in msg :
                        if msg["msg"] in self.usuarios:
                            msg_to_send = {'type': 'verificacion usuario', 'estado': "False"}
                            self.send(msg_to_send, client_socket)
                            print( f"|{a}| Nombre rechazado  | {b}       | ")
                        else:
                            msg_to_send = {'type': 'verificacion usuario', 'estado': msg["msg"]}
                            print( f"|{a}| Nombre aceptado   | {b}       | ")
                            self.send(msg_to_send, client_socket)
                            self.sockets[client_socket]["jugando"] = True
                            self.sockets[client_socket]["nombre"] = msg["msg"]
                            self.usuarios.append(str(msg["msg"]))
                            string_usuarios = ""
                            env = {'type': 'actualizar sala espera', "estado": string_usuarios[1::]}
                            for i in self.usuarios:
                                string_usuarios += "," + str(i)
                            for skt in self.sockets.items():
                                if skt[1]["jugando"] == True:
                                    self.send( env , skt[0])
                                    largo = len(str(env))
                            print( f"|Todos los usuarios| Actualizar sala de espera   | {largo} | ")

                                    
                                    
                            if len(self.usuarios) == data["cantidad_jugadores_partida"]:
                                
                                time.sleep(3)
                                
                                self.juego_en_curso = True
                                env = {'type': 'empezar partida', "estado": self.usuarios}
                                for skt in self.sockets.keys():
                                    if self.sockets[skt]["jugando"] == True:
                                        self.send( env , skt)
                                self.enviar_carta_reverso([["reverso", " "]])
                                for skt in self.sockets.keys():
                                    if self.sockets[skt]["jugando"] == True:
                                        self.repartir_cartas_iniciales(skt)
                                largo = len({'type': 'empezar partida', "estado": self.usuarios})
                                print( f"|Todos los usuarios| Empezar Juego   | {largo}       | ")
                                
                                self.enviar_carta_pozo()
                                self.turno_jugador = self.usuarios[0]
                                self.turno()
                                
                            
                    else: 
                        msg_ = {'type': 'verificacion usuario', 'estado': "No cumple requisitos"}
                        self.send(msg_, client_socket)
                        print( f"|{a}| Nombre rechazado  | {b}       | ")
                else:
                    msg_to_send = {'type': 'verificacion usuario', 'estado': "Partida completa"}
                    self.send(msg_to_send, client_socket)
                    print( f"|{a}| Nombre rechazado  | {b}       | ")
            else:
                msg_to_send = {'type': 'verificacion usuario', 'estado': "Partida en progreso"}
                self.send(msg_to_send, client_socket)
                print( f"|{a}| Nombre rechazado  | {b}| ")
        
        if  msg["tipo"] == "carta jugada":
            nombre = self.sockets[client_socket]["nombre"]
            print( f"|{nombre}| Carta jugada      | {b}| ")

            
            self.revisar_carta_valida(msg["msg"], client_socket)
        if msg["tipo"] == "robar carta":
            nombre = self.sockets[client_socket]["nombre"]
            print( f"|{nombre}| Carta robada      | -                  | ")
            if self.cartas_acumuladas == 0:
                carta_robada = sacar_cartas(1)
            else:
                carta_robada = sacar_cartas(self.cartas_acumuladas)

            self.enviar_carta(carta_robada,client_socket)
            self.turno()
            self.cartas_acumuladas = 0

        if msg["tipo"] == "perdi":
            self.usuarios.remove(self.sockets[client_socket]["nombre"])
            nombre = self.sockets[client_socket]["nombre"]

            print( f"|{nombre}| Perdío :(         | -                  | ")

        if msg["tipo"] == "gritar dcc4":
            nombre = self.sockets[client_socket]["nombre"]
            print( f"|{nombre}| Grito DCCuatro    | -                  | ")

            x = 0
            if msg["msg"][self.sockets[client_socket]["nombre"]] ==1 and self.gritar_dcc4 == False:
                self.gritar_dcc4 == True

            
            else:
                for i in msg["msg"].keys():
                    if msg["msg"][i] == 1 and self.gritar_dcc4 == False:
                        x = 1
                        print("llego antes")
                        self.gritar_dcc4 == True
                        #self.enviar_carta
                if x == 0:
                    print("se equivoco")
        if msg["tipo"] == "carta color":
            self.color = msg["msg"] 
            print( f"|Todos los usuarios| Cambiar Color  |  {self.color}                | ") ####ver si funciojna
            for skt in self.sockets.keys():
                if self.sockets[skt]["jugando"] == True:
                    self.send({'type': 'carta color', "estado": self.color} , skt)



                



            
        

    def revisar_carta_valida(self,carta_, skt):
        self.valida = False
        carta = [carta_[1], carta_[0]]
        if self.cartas_acumuladas == 0:
            if carta[0] == self.carta_pozo[0]:
                self.valida = True
                if carta[0] == "+2":
                    print("sume 2")
                    self.cartas_acumuladas += 2
                if carta[0] == "sentido": 
                    invertir =  self.usuarios[::-1]
                    print(self.usuarios)
                    self.usuarios = invertir
                    print(self.usuarios)

            if carta[1] == self.carta_pozo[1]:
                #if carta[0] == "sentido" and self.carta_pozo[0] == "+2":
                #    self.valida = False
                #else: 
                if carta[0] == "+2":
                    print("sume 2")
                    self.cartas_acumuladas += 2
                self.valida = True
                if carta[0] == "sentido": 
                    invertir =  self.usuarios[::-1]
                    print(self.usuarios)
                    self.usuarios = invertir
                    print(self.usuarios)
            if carta[0] == "color":
                self.valida = True

            #if carta[0] == "+2" and self.carta_pozo[0] == "+2":
            #    self.valida = True
            #    self.cartas_acumuladas += 2
            if self.carta_pozo[0] == "color" and self.color == carta[1]:###arreglar
                self.valida = True
                self.color = "no "
                if carta[0] == "sentido": 
                    invertir =  self.usuarios[::-1]
                    print(self.usuarios)
                    self.usuarios = invertir
                    print(self.usuarios)
                if carta[0] == "+2":
                    print("sume 2")
                    self.cartas_acumuladas += 2
        else: 
            if carta[0] == "+2":
                self.cartas_acumuladas += 2
                self.valida = True
        c = self.sockets[skt]["nombre"]

        if self.valida == True:
            self.carta_pozo = carta
            self.send({'type': 'carta revisada', "estado":"True"} , skt)
            print( f"|{c}| Carta aceptada    | -                  | ")

            
            for skt in self.sockets.keys():          
                if self.sockets[skt]["jugando"] == True:
                    self.send({'type': 'recibir carta pozo', "estado":""} , skt)
            self.enviar_carta_reverso([self.carta_pozo])
            largo = len({'type': 'recibir carta pozo', "estado":""})
            print( f"| Todos los usuarios | Recibir carta pozo  | {largo}  | ")

            for sock in self.sockets.keys():
                self.send({'type': 'restar carta', "estado":self.turno_jugador } , sock)
            self.turno()
            print( f"| Todos los usuarios | Restar carta oponente | {c}  | ")


            
        else:
            self.send({'type': 'carta revisada', "estado":"False"} , skt)
            print( f"|{c }| Carta rechazada   | -                  | ")








    def repartir_cartas_iniciales(self,skt):
        self.enviar_carta(sacar_cartas(data["cartas_iniciales"]), skt)
    def enviar_carta_pozo(self): #para la primera carta del pozo 
        self.carta_pozo_ = sacar_cartas(1)
        self.carta_pozo = self.carta_pozo_[0]
        
        for skt in self.sockets.keys():          
            if self.sockets[skt]["jugando"] == True:
                self.send({'type': 'recibir carta pozo', "estado":""} , skt)
        self.enviar_carta_reverso(self.carta_pozo_)
    
       
    def enviar_carta(self, cartas,skt):
        for carta in cartas:
           
            bytes_para_enviar = bytearray()
            bytes_para_enviar += (1).to_bytes(4, byteorder = "big")
            bytes_color = (carta[1]).encode()
            bytes_para_enviar += (len(bytes_color)).to_bytes(4, byteorder = "little")
            bytes_para_enviar += bytes_color
            bytes_para_enviar+= (2).to_bytes(4, byteorder = "big")
            tipo_carta = (carta[0]).encode("UTF-8")
            bytes_para_enviar += (len(tipo_carta)).to_bytes(4, byteorder = "little")
            bytes_para_enviar += tipo_carta
            bytes_para_enviar += (3).to_bytes(4, byteorder = "big")
            if carta[0] == "color" or carta[0] == "reverso" :
                path_imagen = f"simple/{carta[0]}.png"

            else:
                path_imagen = f"simple/{carta[0]}_{carta[1]}.png"

            with open(path_imagen, "rb") as image:
                bytes_imagen_  = base64.b64encode(image.read())
                bytes_imagen1 = bytes_imagen_.decode("UTF-8")
                bytes_imagen = (bytes_imagen1).encode("UTF-8")

                #bytes_imagen = bytes_imagen.encode("UTF-8")
            
           
            bytes_para_enviar += (len(bytes_imagen)).to_bytes(4, byteorder = "little")
            bytes_para_enviar += bytes_imagen
            largo_mensaje = (len(bytes_para_enviar)).to_bytes(4, byteorder = "big")

            bytes_para_enviar = largo_mensaje + bytes_para_enviar
            for sock in self.sockets.keys():
                #if skt != sock:
                time.sleep(0.5)
                self.send({'type': 'sumar carta', "estado": self.sockets[skt]["nombre"]} , sock)
            
            self.send({'type': 'recibir carta mano', "estado":""} , skt)
            skt.send(bytes_para_enviar)
            nombre = self.sockets[skt]["nombre"]
            print( f"|{nombre}| carta enviada mano    | {carta} , {len(bytes_para_enviar)}| ")
            print( f"| Todos los usuarios | Sumar carta oponente | {nombre}  | ")


           
 
    def enviar_carta_reverso(self, cartas):
        for carta in cartas:
            bytes_para_enviar = bytearray()
            bytes_para_enviar += (1).to_bytes(4, byteorder = "big")
            bytes_color = (carta[1]).encode()
            bytes_para_enviar += (len(bytes_color)).to_bytes(4, byteorder = "little")
            bytes_para_enviar += bytes_color
            bytes_para_enviar+= (2).to_bytes(4, byteorder = "big")
            tipo_carta = (carta[0]).encode("UTF-8")
            bytes_para_enviar += (len(tipo_carta)).to_bytes(4, byteorder = "little")
            bytes_para_enviar += tipo_carta
            bytes_para_enviar += (3).to_bytes(4, byteorder = "big")
            if carta[0] == "color" or carta[0] == "reverso" :
                path_imagen = f"simple/{carta[0]}.png"

            else:
                path_imagen = f"simple/{carta[0]}_{carta[1]}.png"

            with open(path_imagen, "rb") as image:
                bytes_imagen_  = base64.b64encode(image.read())
                bytes_imagen1 = bytes_imagen_.decode("UTF-8")
                bytes_imagen = (bytes_imagen1).encode("UTF-8")

                #bytes_imagen = bytes_imagen.encode("UTF-8")
            bytes_para_enviar += (len(bytes_imagen)).to_bytes(4, byteorder = "little")
            bytes_para_enviar += bytes_imagen
            largo_mensaje = (len(bytes_para_enviar)).to_bytes(4, byteorder = "big")

            bytes_para_enviar = largo_mensaje + bytes_para_enviar
            for skt in self.sockets.items():
                if skt[1]["jugando"] == True:
                    time.sleep(1)
                    skt[0].send(bytes_para_enviar)
            j = self.turno_jugador
            print( f"|{j}| Carta enviada pozo    | {carta}, {len(bytes_para_enviar)}| ")

                   
    def turno(self):
        if self.turno_jugador == self.usuarios[-1]:
            self.turno_jugador = self.usuarios[0]
        else:
            self.turno_jugador = self.usuarios[self.usuarios.index(self.turno_jugador) + 1]
        for sock in self.sockets.keys():  
            self.send({"type": "cambio turno", "estado": self.turno_jugador} , sock)
        print( f"|                    | Cambio turno    | {self.turno_jugador}| ")


        
    def send(self, value, sock):
        str_value = str(value)
        msg_bytes = str_value.encode()
        sock.send(msg_bytes)

#-----------------------------------------------------------------------------------

if __name__ == '__main__':
    port = data["port"]
    host = data["host"]
    server = Servidor(port, host)

#-----------------------------------------------------------------------------------

