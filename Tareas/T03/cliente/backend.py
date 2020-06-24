from PyQt5.QtCore import QObject, pyqtSignal

class BackEnd(QObject):
    senal_usuario_verificado = pyqtSignal(str)
    senal_sala_de_espera = pyqtSignal(str)
    senal_enviar_mensaje_servidor = pyqtSignal(dict)
    def __init__(self,*args):
        super().__init__(*args)
    
    def enviar(self, msg):
        self.senal_enviar_mensaje_servidor.emit(msg)
    
    def recibir_mensaje(self, msg):
        if msg["type"] == "verificacion usuario":
            self.senal_usuario_verificado.emit(msg["estado"])
            #if msg["estado"] == "True":
             #  self.senal_sala_de_espera.emit(msg["estado"])
        if msg["type"] == "actualizar sala espera":
            self.senal_sala_de_espera.emit(msg["estado"])

        

    def nombre_usuario(self, nombre):
        self.nombre = nombre["msg"]
        self.enviar(nombre)



