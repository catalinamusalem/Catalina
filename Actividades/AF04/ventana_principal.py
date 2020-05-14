import os
import sys
from random import choice

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication


class VentanaPrincipal(QWidget):

    # Aquí debes crear una señal que usaras para enviar la jugada al back-end
    senal_enviar_jugada = pyqtSignal(dict)

    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()


    def crear_pantalla(self):
        # Aquí deben crear la ventana vacia.
        self.setWindowTitle("DCCuent")
        # Es decir, agregar y crear labels respectivos a datos del juego, pero sin contenido
        nombre = ""
        vict = ""
        derrot = ""
        self.rutai=""
        self.rutar=""
        self.rutaa=""
        self.pixeles_i= ""
        self.pixeles_r= ""
        self.pixeles_a= ""
        self.nombre_usuario= QLabel(nombre,self)
        self.victorias =QLabel(vict,self)
        self.derrotas = QLabel(derrot,self)
        self.infanteria = QLabel("Q", self)
        self.rango=QLabel("W",self)
        self.artilleria=QLabel("E",self)
        self.logo_i = QLabel(self)
        self.logo_r = QLabel(self)
        self.logo_a = QLabel(self)
        pix_i=QPixmap(self.rutai)
        pix_r=QPixmap(self.rutar)
        pix_a=QPixmap(self.rutaa)
        self.logo_i.setPixmap(pix_i)
        self.logo_r.setPixmap(pix_r)
        self.logo_a.setPixmap(pix_a)

        vlayout1 = QVBoxLayout()
        vlayout1.addWidget(self.nombre_usuario)
        vlayout1.addWidget(self.infanteria)
        vlayout1.addWidget(self.logo_i)

        vlayout2 = QVBoxLayout()
        vlayout2.addWidget(self.victorias)
        vlayout2.addWidget(self.rango)
        vlayout2.addWidget(self.logo_r)

        vlayout3 = QVBoxLayout()
        vlayout3.addWidget(self.derrotas)
        vlayout3.addWidget(self.artilleria)
        vlayout3.addWidget(self.logo_a)

        mainlayout = QHBoxLayout()
        mainlayout.addLayout(vlayout1)
        mainlayout.addLayout(vlayout2)
        mainlayout.addLayout(vlayout3)
        self.setLayout(mainlayout)

        # Si usas layout recuerda agregar los labels al layout y finalmente setear el layout
        

    def actualizar(self, datos):
        # Esta es la funcion que se encarga de actualizar el contenido de la ventana y abrirla
        # Recibe las nuevas cartas y la puntuación actual en un diccionario
        nombre = datos["usuario"]
        vict = datos["victorias"]
        derrot = datos["derrotas"]
        self.pixeles_i= datos["infanteria"]
        self.pixeles_r= datos["rango"]
        self.pixeles_a= datos["artilleria"]
        self.rutai=datos["infanteria"]["ruta"]
        self.rutar=datos["rango"]["ruta"]
        self.rutaa=datos["artilleria"]["ruta"]

    

        # Al final, se muestra la ventana.
        self.show()

    def keyPressEvent(self, evento):
        # Aquí debes capturar la techa apretara,
        # y enviar la carta que es elegida
        if evento.text() == "q":
            data= self.pixeles_i
            self.senal_enviar_jugada.emit(data)
        if evento.text() == "w":
            data= self.pixeles_r
            self.senal_enviar_jugada.emit(data)
        if evento.text() == "e":
            data= self.pixeles_a
            self.senal_enviar_jugada.emit(data)




class VentanaCombate(QWidget):

    # Esta señal es para volver a la VentanaPrincipal con los datos actualizados
    senal_regresar = pyqtSignal(dict)
    # Esta señal envia a la ventana final con el resultado del juego
    senal_abrir_ventana_final = pyqtSignal(str)

    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()

    def crear_pantalla(self):
        self.setWindowTitle("DCCuent")
        self.vbox = QVBoxLayout()
        self.layout_principal = QHBoxLayout()
        self.label_carta_usuario = QLabel()
        self.label_victoria = QLabel()
        self.label_carta_enemiga = QLabel()
        self.boton_regresar = QPushButton("Regresar")

        self.layout_principal.addWidget(self.label_carta_usuario)
        self.layout_principal.addWidget(self.label_victoria)
        self.layout_principal.addWidget(self.label_carta_enemiga)

        self.boton_regresar.clicked.connect(self.regresar)
        self.vbox.addLayout(self.layout_principal)
        self.vbox.addWidget(self.boton_regresar)

        self.setLayout(self.vbox)

    def mostrar_resultado_ronda(self, datos):
        self.datos = datos
        mensaje = datos["mensaje"]
        carta_enemiga = datos["enemigo"]
        carta_jugador = datos["jugador"]
        self.label_carta_usuario.setPixmap(QPixmap(carta_jugador["ruta"]).scaled(238,452))
        self.label_carta_enemiga.setPixmap(QPixmap(carta_enemiga["ruta"]).scaled(238,452))
        self.label_victoria.setText(mensaje)
        self.show()

    def regresar(self):
        resultado = self.datos["resultado"]
        if resultado == "victoria" or resultado == "derrota":
            self.senal_abrir_ventana_final.emit(resultado)
        else:
            self.senal_regresar.emit(self.datos)
        self.hide()


if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()

    ventana_principal.show()
    sys.exit(a.exec())
