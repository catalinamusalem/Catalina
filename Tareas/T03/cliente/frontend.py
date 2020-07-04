import sys
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap, QDrag, QPainter, QCursor, QTransform
from PyQt5.QtWidgets import QApplication
import json
import time
with open("parametros.json") as f:
    data = json.load(f)
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
        pixeles=QPixmap(data["ruta_logo_inicio"]).scaled(largo_logo, ancho_logo,Qt.KeepAspectRatio)
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
        self.senal_verificar_nombre.emit({"tipo": "nombre", "msg": self.ingresar_nombre.text()})
    def resultado_usuario(self, estado):
        if estado == self.ingresar_nombre.text():
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
        pixeles=QPixmap(data["ruta_logo_inicio"]).scaled(largo_logo, ancho_logo,Qt.KeepAspectRatio)
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
        jugadores_=(jugadores1).split(",")
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
    def empezar_partida(self):
        self.hide()
    def salir(self, event):
        sys.exit()
class ElegirColor(QWidget):
    senal_cambiar_color = pyqtSignal(str)
    def __init__ (self, *args):
        super().__init__(*args)
        self.crear_pantalla()
    def crear_pantalla(self):
        self.setWindowTitle("Elegir Color")
        self.boton_azul = QPushButton("AZUL",self)
        self.boton_rojo = QPushButton("ROJO",self)
        self.boton_amarillo = QPushButton("AMARILLO",self)
        self.boton_verde = QPushButton("VERDE",self)
        self.boton_azul.clicked.connect(self.azul)
        self.boton_rojo.clicked.connect(self.rojo)
        self.boton_amarillo.clicked.connect(self.amarillo)
        self.boton_verde.clicked.connect(self.verde)
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_1.addWidget(self.boton_azul)
        layout_1.addWidget(self.boton_rojo)
        layout_2.addWidget(self.boton_verde)
        layout_2.addWidget(self.boton_amarillo)
        main_layout = QVBoxLayout()
        main_layout.addLayout(layout_1)
        main_layout.addLayout(layout_2)
        self.setLayout(main_layout)
    def azul(self):
        self.senal_cambiar_color.emit("azul")
        self.hide()
    def rojo(self):
        self.senal_cambiar_color.emit("rojo")
        self.hide()
    def amarillo(self):
        self.senal_cambiar_color.emit("amarillo")
        self.hide()
    def verde(self):
        self.senal_cambiar_color.emit("verde")
        self.hide()
    def mostrar(self):
        self.show()

class VentanaPrincipal(QWidget):
    senal_jugar_carta = pyqtSignal(list)
    senal_robar_carta = pyqtSignal()
    senal_gritar_dcc4 = pyqtSignal()
    senal_elegir_color = pyqtSignal()
    def __init__ (self, *args):
        super().__init__(*args)
        self.cartas_jugador_1 = [] #JUGADOR PROPIO
        self.cartas_jugador_2 = []
        self.cartas_jugador_3 = []
        self.cartas_jugador_4 = []
        self.crear_pantalla()
    def crear_pantalla(self):
        self.setWindowTitle("Ventana Prinicipal")
        self.pozo = QLabel(self)
        self.pozo.setGeometry(1050,595,321,450)
        self.pozo.setScaledContents(True)
        #self.pozo.move(1050, 590)
        self.turno_de = QLabel("TURNO DE:",self)
        self.turno_de_ = QLabel(" ",self)
        self.color = QLabel("COLOR:",self)
        self.color_ = QLabel("",self)
        self.robar_carta = QLabel(self)
        self.robar_carta.setGeometry(2650, 550, 391,550)
        self.boton_robar_carta = QPushButton("ROBA 1 CARTA",self)
        self.gritar = QLabel("GRITA",self)
        self.boton_gritar = QPushButton("¡DCCUATRO!",self)
        self.turno_de.move(2650,200)
        self.turno_de_.move(2800,200)
        self.color.move(2650,300)
        self.color_.move(2800,300)
        self.robar_carta.move(2650,550)
        self.boton_robar_carta.move(2750,1120)
        self.boton_robar_carta.clicked.connect(self.robar_carta_)
        self.boton_gritar.clicked.connect(self.gritar_dcc4)
        self.gritar.move(2800, 1400)
        self.boton_gritar.move(2750, 1450)
        self.carta_jugador_1_1  = QLabel(self)
        self.carta_jugador_1_2  = QLabel(self)
        self.carta_jugador_1_3  = QLabel(self)
        self.carta_jugador_1_4  = QLabel(self)
        self.carta_jugador_1_5  = QLabel(self)
        self.carta_jugador_1_6  = QLabel(self)
        self.carta_jugador_1_7  = QLabel(self)
        self.carta_jugador_1_8  = QLabel(self)
        self.carta_jugador_1_9  = QLabel(self)
        self.carta_jugador_1_10 = QLabel(self)
        self.carta_jugador_2_1  = QLabel(self)
        self.carta_jugador_2_2  = QLabel(self)
        self.carta_jugador_2_3  = QLabel(self)
        self.carta_jugador_2_4  = QLabel(self)
        self.carta_jugador_2_5  = QLabel(self)
        self.carta_jugador_2_6  = QLabel(self)
        self.carta_jugador_2_7  = QLabel(self)
        self.carta_jugador_2_8  = QLabel(self)
        self.carta_jugador_2_9  = QLabel(self)
        self.carta_jugador_2_10 = QLabel(self)
        self.carta_jugador_3_1  = QLabel(self)
        self.carta_jugador_3_2  = QLabel(self)
        self.carta_jugador_3_3  = QLabel(self)
        self.carta_jugador_3_4  = QLabel(self)
        self.carta_jugador_3_5  = QLabel(self)
        self.carta_jugador_3_6  = QLabel(self)
        self.carta_jugador_3_7  = QLabel(self)
        self.carta_jugador_3_8  = QLabel(self)
        self.carta_jugador_3_9  = QLabel(self)
        self.carta_jugador_3_10 = QLabel(self)
        self.carta_jugador_4_1  = QLabel(self)
        self.carta_jugador_4_2  = QLabel(self)
        self.carta_jugador_4_3  = QLabel(self)
        self.carta_jugador_4_4  = QLabel(self)
        self.carta_jugador_4_5  = QLabel(self)
        self.carta_jugador_4_6  = QLabel(self)
        self.carta_jugador_4_7  = QLabel(self)
        self.carta_jugador_4_8  = QLabel(self)
        self.carta_jugador_4_9  = QLabel(self)
        self.carta_jugador_4_10 = QLabel(self)
        self.cartas_jugador_1.append(self.carta_jugador_1_1) 
        self.cartas_jugador_1.append(self.carta_jugador_1_2) 
        self.cartas_jugador_1.append(self.carta_jugador_1_3) 
        self.cartas_jugador_1.append(self.carta_jugador_1_4) 
        self.cartas_jugador_1.append(self.carta_jugador_1_5) 
        self.cartas_jugador_1.append(self.carta_jugador_1_6) 
        self.cartas_jugador_1.append(self.carta_jugador_1_7) 
        self.cartas_jugador_1.append(self.carta_jugador_1_8) 
        self.cartas_jugador_1.append(self.carta_jugador_1_9) 
        self.cartas_jugador_1.append(self.carta_jugador_1_10) 
        self.cartas_jugador_2.append(self.carta_jugador_2_1) 
        self.cartas_jugador_2.append(self.carta_jugador_2_2) 
        self.cartas_jugador_2.append(self.carta_jugador_2_3) 
        self.cartas_jugador_2.append(self.carta_jugador_2_4) 
        self.cartas_jugador_2.append(self.carta_jugador_2_5) 
        self.cartas_jugador_2.append(self.carta_jugador_2_6) 
        self.cartas_jugador_2.append(self.carta_jugador_2_7) 
        self.cartas_jugador_2.append(self.carta_jugador_2_8) 
        self.cartas_jugador_2.append(self.carta_jugador_2_9) 
        self.cartas_jugador_2.append(self.carta_jugador_2_10) 
        self.cartas_jugador_3.append(self.carta_jugador_3_1) 
        self.cartas_jugador_3.append(self.carta_jugador_3_2) 
        self.cartas_jugador_3.append(self.carta_jugador_3_3) 
        self.cartas_jugador_3.append(self.carta_jugador_3_4) 
        self.cartas_jugador_3.append(self.carta_jugador_3_5) 
        self.cartas_jugador_3.append(self.carta_jugador_3_6) 
        self.cartas_jugador_3.append(self.carta_jugador_3_7) 
        self.cartas_jugador_3.append(self.carta_jugador_3_8) 
        self.cartas_jugador_3.append(self.carta_jugador_3_9) 
        self.cartas_jugador_3.append(self.carta_jugador_3_10) 
        self.cartas_jugador_4.append(self.carta_jugador_4_1) 
        self.cartas_jugador_4.append(self.carta_jugador_4_2) 
        self.cartas_jugador_4.append(self.carta_jugador_4_3) 
        self.cartas_jugador_4.append(self.carta_jugador_4_4) 
        self.cartas_jugador_4.append(self.carta_jugador_4_5) 
        self.cartas_jugador_4.append(self.carta_jugador_4_6) 
        self.cartas_jugador_4.append(self.carta_jugador_4_7) 
        self.cartas_jugador_4.append(self.carta_jugador_4_8) 
        self.cartas_jugador_4.append(self.carta_jugador_4_9) 
        self.cartas_jugador_4.append(self.carta_jugador_4_10) 
        for i in range(5):
            self.cartas_jugador_1[i].setGeometry(700 + 213*i, 1350, 213,300)
            self.cartas_jugador_1[i+5].setGeometry(700 + 213*i, 1050, 213, 300)
            self.cartas_jugador_2[i+5].setGeometry(700 + 213*i, 300,213,300)
            self.cartas_jugador_2[i].setGeometry(700 + 213*i, 0, 213,300)
            self.cartas_jugador_3[i].setGeometry(45, 400+213*i,300,213)
            self.cartas_jugador_3[i+5].setGeometry(345 , 400+ 213*i,300, 213)
            self.cartas_jugador_4[i].setGeometry(1800,  400+200*i,300,213)
            self.cartas_jugador_4[i+5].setGeometry(2100, 400+ 200*i,300,213)
            self.cartas_jugador_1[i].setScaledContents(True)
            self.cartas_jugador_1[i+5].setScaledContents(True)
            self.cartas_jugador_2[i].setScaledContents(True)
            self.cartas_jugador_2[i+5].setScaledContents(True)
            self.cartas_jugador_3[i].setScaledContents(True)
            self.cartas_jugador_3[i+5].setScaledContents(True)
            self.cartas_jugador_4[i].setScaledContents(True)
            self.cartas_jugador_4[i+5].setScaledContents(True)

    def empezar_partida(self, usuarios, nombre_propio):
        i = 0
        self.usuarios = usuarios
        self.nombre_propio = nombre_propio
        self.cartas_jugador = [0,0,0,0,0,0,0,0,0,0] #para saber que tipo y numero de carta hay en cada espacio
        for usuarios in self.usuarios.keys():
            if usuarios == self.nombre_propio:
                self.usuarios[usuarios] = [0,0,0,0,0,0,0,0,0,0, self.cartas_jugador_1 ] #los ceros son para saber si esta ocupado el espacio de la carta
            else:
                if i == 0:
                    self.usuarios[usuarios] = [self.cartas_jugador_2 ]
                if i == 1:
                    self.usuarios[usuarios] = [self.cartas_jugador_3 ]
                if i == 2:
                    self.usuarios[usuarios] = [self.cartas_jugador_4 ]
                i += 1
        self.show()
    def recibir_carta_reverso(self, imagen):
        self.carta_reverso = imagen
        pixmap = QPixmap()
        pixmap.loadFromData(imagen, 'png')
        girar_der = QTransform()
        girar_der.rotate(90)
        girar_izq = QTransform()
        girar_izq.rotate(270)
        girar_180 = QTransform()
        girar_180.rotate(180)
        pixmap_girado_der = pixmap.transformed(girar_der)
        pixmap_girado_izq = pixmap.transformed(girar_izq)
        pixmap_girado_180 = pixmap.transformed(girar_180)
        self.robar_carta.setPixmap(pixmap)
        for i in range(10):
            self.cartas_jugador_2[i].setPixmap(pixmap_girado_180)
            self.cartas_jugador_3[i].setPixmap(pixmap_girado_der)
            self.cartas_jugador_4[i].setPixmap(pixmap_girado_izq)
            self.cartas_jugador_2[i].hide()
            self.cartas_jugador_3[i].hide()
            self.cartas_jugador_4[i].hide()
    def recibir_carta_mano(self, imagen, color, tipo):
        cartas = self.usuarios[self.nombre_propio][0]
        for i in range(10):
            if self.usuarios[self.nombre_propio][i] == 0:
                self.usuarios[self.nombre_propio][i] = 1
                self.cartas_jugador[i] = [color , tipo]
                pixmap = QPixmap()
                pixmap.loadFromData(imagen, 'png')
                self.cartas_jugador_1[i].setPixmap(pixmap)
                self.cartas_jugador_1[i].show()
                break
    def recibir_carta_pozo(self, imagen,color,tipo):
        pixmap = QPixmap()
        pixmap.loadFromData(imagen, 'png')
        self.pozo.setPixmap(pixmap)
        self.carta_pozo = [color, tipo]
        self.color_.setText(color)
        self.color_.adjustSize()
    def cartas_jugadores(self, jugadores):      
        for nombre in jugadores.keys():
            if nombre != self.nombre_propio:
                for j in range(jugadores[nombre]):
                    self.usuarios[nombre][0][j].show()
                for k in range(10- jugadores[nombre]):
                    self.usuarios[nombre][0][9-k].hide()   
    def recibir_turno(self, nombre):
        self.turno = nombre
        self.turno_de_.setText(nombre)
        self.turno_de_.adjustSize()
    def mousePressEvent(self,event):
        self.jugar_carta = False
        x = event.x()
        y = event.y()
        if y in range(1350,1650):
            if x in range(700, 913):
                self.jugar_carta = self.cartas_jugador[0]
            if x in range(913, 1126):
                self.jugar_carta = self.cartas_jugador[1]
            if x in range(1126, 1339):
                self.jugar_carta = self.cartas_jugador[2]
            if x in range(1339, 1552):
                self.jugar_carta = self.cartas_jugador[3]
            if x in range(1552, 1765):
                self.jugar_carta = self.cartas_jugador[4]
        if y in range(1050,1350):
            if x in range(700, 913):
                self.jugar_carta = self.cartas_jugador[5]
            if x in range(913, 1126):
                self.jugar_carta = self.cartas_jugador[6]
            if x in range(1126, 1339):
                self.jugar_carta = self.cartas_jugador[7]
            if x in range(1339, 1552):
                self.jugar_carta = self.cartas_jugador[8]
            if x in range(1552, 1765):
                self.jugar_carta = self.cartas_jugador[9]
        if self.jugar_carta != False:
            self.senal_jugar_carta.emit(self.jugar_carta)
    def carta_jugada(self):
        indice = self.cartas_jugador.index(self.jugar_carta)
        if self.cartas_jugador[indice][1] == "color":
            self.senal_elegir_color.emit()
        self.cartas_jugador[indice] = 0
        self.usuarios[self.nombre_propio][indice] = 0
        self.usuarios[self.nombre_propio][10][indice].hide()
    def robar_carta_(self):
        self.senal_robar_carta.emit()
    def gritar_dcc4(self):
        self.senal_gritar_dcc4.emit()
    def color_elegido(self, color):
        self.color_.setText(color)
        self.color_.adjustSize()
if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    a = QApplication(sys.argv)
    ventana_inicio = ElegirColor()
    ventana_inicio.show()
    sys.exit(a.exec())