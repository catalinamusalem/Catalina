import sys
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
import json

with open("parametros.json") as f:
    data = json.load(f)
    print(data)

class VentanaInicio(QWidget):
    senal_verificar_nombre = pyqtSignal(dict)
    

    def __init__ (self, *args):
        super().__init__(*args)
        self.crear_pantalla()
    def crear_pantalla(self):
        self.setWindowTitle("Ventana de Inicio")
        main_layout = QVBoxLayout()
        self.logo_inicio = QLabel(self)
        ancho_logo = 700
        largo_logo = 700
        pixeles = QPixmap(data["ruta_logo_inicio"]).scaled(largo_logo, ancho_logo, Qt.KeepAspectRatio)
        self.logo_inicio.setPixmap(pixeles)
        main_layout.addWidget(self.logo_inicio)
        self.bienvenida = QLabel('INGRESE SU NOMBRE DE USUARIO', self)
        main_layout.addWidget(self.bienvenida)
        self.ingresar_nombre = QLineEdit("", self)
        self.boton_entrar = QPushButton("ENTRAR",self)
        self.boton_entrar.setStyleSheet('QPushButton {background-color: red; color: black;}')
        self.mensaje = QLabel(" ", self)
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.ingresar_nombre)
        layout_botones.addWidget(self.boton_entrar)
        main_layout.addLayout(layout_botones)
        main_layout.addWidget(self.mensaje)
        self.setLayout(main_layout)
        self.boton_entrar.clicked.connect(self.verificar_nombre)

    def verificar_nombre(self):
        print(self.ingresar_nombre.text())
        self.senal_verificar_nombre.emit({"tipo": "nombre", "msg": self.ingresar_nombre.text()})
    def resultado_usuario(self, estado):
        if estado == "True":
            self.hide()
        if estado == "False":
            self.mensaje.setText("El nombre ya está ocupado, intenta con otro")
        if estado == "No cumple requisitos":
            self.mensaje.setText("El nombre solo debe contener letras y numeros")
        if estado == "Partida completa":
            self.mensaje.setText("La partida no tiene espacio para mas jugadores :(")
        if estado == "Partida en progreso":
            self.mensaje.setText("Ya hay un juego en curso, debes esperar hasta que termine")
        
     

        
        
class SalaDeEspera(QWidget):
    

    def __init__ (self, *args):
        super().__init__(*args)
        self.jugadores_ = []
        self.crear_pantalla()
    def crear_pantalla(self):
        self.setWindowTitle("Sala de Espera")
        main_layout = QVBoxLayout()
        self.logo_inicio = QLabel(self)
        ancho_logo = 700
        largo_logo = 700
        pixeles = QPixmap(data["ruta_logo_inicio"]).scaled(largo_logo, ancho_logo, Qt.KeepAspectRatio)
        self.logo_inicio.setPixmap(pixeles)
        main_layout.addWidget(self.logo_inicio)
        self.conectarse = QLabel('JUGADORES CONECTADOS', self)
        main_layout.addWidget(self.conectarse)
        layout_jugadores_1 = QHBoxLayout()
        layout_jugadores_2 = QHBoxLayout()
        self.jugador_1 = QLabel('Esperando...', self)
        self.jugador_2 = QLabel("Esperando...",self)
        self.jugador_3 = QLabel("Esperando...",self)
        self.jugador_4 = QLabel("Esperando...",self)
        layout_jugadores_1.addWidget(self.jugador_1)
        layout_jugadores_1.addWidget(self.jugador_2)
        layout_jugadores_2.addWidget(self.jugador_3)
        layout_jugadores_2.addWidget(self.jugador_4)
        main_layout.addLayout(layout_jugadores_1)
        main_layout.addLayout(layout_jugadores_2)
        self.setLayout(main_layout)

    def jugadores(self, jugadores1):
        #self.jugadores_.append(jugadores)
        print(jugadores1)
        jugadores_=(jugadores1).split(",")
        print(jugadores_)
        if len(jugadores_) == 1:
            self.jugador_1.setText(jugadores_[0])
        if len(jugadores_) == 2:
            self.jugador_1.setText(jugadores_[0])
            self.jugador_3.setText(jugadores_[1])
        if len(jugadores_) == 3:
            self.jugador_1.setText(jugadores_[0])
            self.jugador_3.setText(jugadores_[1])
            self.jugador_2.setText(jugadores_[2])
        if len(jugadores_) == 4:
            self.jugador_1.setText(jugadores_[0])
            self.jugador_3.setText(jugadores_[1])
            self.jugador_2.setText(jugadores_[2])
            self.jugador_4.setText(jugadores_[3])
        self.show()



    def salir(self, event):
        sys.exit()

    



if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    ventana_inicio = VentanaInicio()

    ventana_inicio.show()
    sys.exit(a.exec())