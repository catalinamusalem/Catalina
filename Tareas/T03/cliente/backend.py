from PyQt5.QtCore import QObject, pyqtSignal
import json
import base64

with open("parametros.json") as f:
    parametros = json.load(f)
class BackEnd(QObject):
    senal_usuario_verificado = pyqtSignal(str)
    senal_sala_de_espera = pyqtSignal(str)
    senal_enviar_mensaje_servidor = pyqtSignal(dict)
    senal_empezar_partida = pyqtSignal()
    senal_empezar_partida_vp = pyqtSignal(dict,str)
    senal_recibir_carta = pyqtSignal(str)
    senal_enviar_carta_reverso = pyqtSignal(bytearray)
    senal_enviar_carta_mano = pyqtSignal(bytearray, str,str)
    senal_enviar_carta_pozo = pyqtSignal(bytearray,str,str)
    senal_cartas_jugadores = pyqtSignal(dict)
    senal_cambiar_turno = pyqtSignal(str)
    senal_carta_jugada = pyqtSignal()
    senal_actualizar_color = pyqtSignal(str)
    def __init__(self,*args):
        super().__init__(*args)
        self.recibir_carta = False
        self.bytes = bytearray()
        self.numero_mensaje = 0
        self.perdi = False
         
    
    def enviar(self, msg):
        self.senal_enviar_mensaje_servidor.emit(msg)
        
    
    def recibir_mensaje(self, data):
        
        print(data[0:70])

        if self.recibir_carta == False and self.perdi == False:
            decoded_data = data.decode()
            decoded_data = decoded_data.replace('\'', '\"') 
            msg = json.loads(decoded_data)
            if msg["type"] == "verificacion usuario":
                self.nombre = msg["estado"]
                self.senal_usuario_verificado.emit(msg["estado"])
                #if msg["estado"] == "True":
                #  self.senal_sala_de_espera.emit(msg["estado"])
            if msg["type"] == "actualizar sala espera":
                self.senal_sala_de_espera.emit(msg["estado"])
            if msg["type"] == "empezar partida":
                self.recibir_carta = True
                self.senal_empezar_partida.emit()
                self.jugadores = {}
                for i in msg["estado"]:
                    self.jugadores[i] = 0
                jugadores = self.jugadores.copy()
                self.senal_empezar_partida_vp.emit(jugadores, self.nombre)
                self.tipo_carta = "reverso"
            if msg["type"] == "recibir carta mano":
                if self.perdi == False:
                    self.recibir_carta = True
                    self.tipo_carta = "mano"
            if msg["type"] == "sumar carta": # o restar 
                self.jugadores[msg["estado"]] += 1
                
                if self.jugadores[self.nombre] == parametros["maximo_cartas"] + 1:
                    self.enviar({"tipo": "perdi", "msg": ""})
                    self.perdi = True
                    print("perdi")
                if self.perdi == False:
                    self.senal_cartas_jugadores.emit(self.jugadores)


            if msg["type"] == "restar carta": # o restar 
                self.jugadores[msg["estado"]] -= 1
                self.senal_cartas_jugadores.emit(self.jugadores)
            
            if msg["type"] == "recibir carta pozo":
                self.tipo_carta = "pozo"
                self.recibir_carta = True
            if msg["type"] == "cambio turno":
                self.turno = msg["estado"]
                self.senal_cambiar_turno.emit(msg["estado"])
                print(self.turno, "cambio")
            if msg["type"] == "carta revisada":
                if msg["estado"] == "True" and self.perdi == False:
                    self.senal_carta_jugada.emit()
            if msg["type"] == "carta color":
                self.senal_actualizar_color.emit(msg["estado"])


            
            
            
            

        else:
            #decoded_data = data.decode()
            #decoded_data = decoded_data.replace('\'', '\"') 
            
            if self.numero_mensaje == 0:
        
                self.largo_mensaje = int.from_bytes(data[0:4], byteorder = "big")
                self.numero_mensaje +=1
                self.bytes += data[4::]
            else:
          
                self.bytes += data
           

            if len(self.bytes) == self.largo_mensaje:
                self.aceptar_carta(self.bytes)
                self.recibir_carta = False 
                self.numero_mensaje = 0
         
    def aceptar_carta(self, carta):
      
        if int.from_bytes(self.bytes[0:4], byteorder = "big") == 1:
            largo_color = int.from_bytes(self.bytes[4:8], byteorder = "little")
            color = (self.bytes[8: 8 + largo_color]).decode()
            
        if int.from_bytes(self.bytes[8 + largo_color:12 + largo_color], byteorder = "big") == 2:
            largo_tipo=int.from_bytes(self.bytes[12+largo_color:16+largo_color],byteorder="little")
            tipo = (self.bytes[16 + largo_color: 16 + largo_color + largo_tipo]).decode()
        d = 16+largo_color+largo_tipo:20+largo_color+largo_tipo
        e = 20 + largo_color + largo_tipo: 24 + largo_color + largo_tipo
        if int.from_bytes(self.bytes[d],byteorder="big")==3:
            largo_imagen = int.from_bytes(self.bytes[e], byteorder = "little")
            pixeles_imagen = bytearray()
            comienzo =  24 + largo_color + largo_tipo
            for i in range(0, (largo_imagen), 32):
                segmento = self.bytes[comienzo + i : comienzo + i + min(32, abs(i - largo_imagen))]
                pixeles_imagen += base64.b64decode(segmento)
        
        if self.tipo_carta == "reverso":
            self.senal_enviar_carta_reverso.emit(pixeles_imagen)
        if self.tipo_carta == "mano":
            self.senal_enviar_carta_mano.emit(pixeles_imagen,color,tipo)
        if self.tipo_carta == "pozo":
            self.carta_pozo = [color, tipo]
            self.senal_enviar_carta_pozo.emit(pixeles_imagen,color,tipo)
        
        self.largo_mensaje = 0
        self.bytes = bytearray()
        
 

    def nombre_usuario(self, nombre):
        self.nombre = nombre["msg"]
        self.enviar(nombre)
    def jugar_carta(self, carta):
        print(self.turno, self.nombre)
        if self.turno == self.nombre and self.perdi == False:
            print(carta)
            self.enviar({"tipo": "carta jugada", "msg": carta})
    def robar_carta(self):
        if self.turno == self.nombre and self.perdi == False:
            self.enviar({"tipo": "robar carta", "msg": ""})
    def gritar_dcc4(self):
        if self.perdi == False:
            self.enviar({"tipo": "gritar dcc4", "msg": self.jugadores})
    def color(self,color):
        self.enviar({"tipo": "carta color", "msg": color})





