import sys

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
import p


class VentanaInicio(QWidget):

    senal_cargar_mapa = pyqtSignal()
    senal_crear_partida = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()

    def crear_pantalla(self):
        self.setWindowTitle("Ventana de Inicio")
        main_layout = QVBoxLayout()
        self.logo_inicio = QLabel(self)
        ancho_logo = p.A_LOGO_INICIO
        largo_logo = p.L_LOGO_INICIO
        pixeles = QPixmap(p.RUTA_LOGO_INICIO).scaled(largo_logo, ancho_logo, Qt.KeepAspectRatio)
        self.logo_inicio.setPixmap(pixeles)
        main_layout.addWidget(self.logo_inicio)
        self.bienvenida = QLabel('¡Bienvenid@ al mejor café virtual del DCC!', self)
        main_layout.addWidget(self.bienvenida)
        self.boton_continuar = QPushButton("Seguir jugando",self)
        self.boton_nueva = QPushButton("Comenzar de nuevo",self)
        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.boton_continuar)
        layout_botones.addWidget(self.boton_nueva)
        main_layout.addLayout(layout_botones)
        self.setLayout(main_layout)
        self.boton_continuar.clicked.connect(self.cargar_mapa)
        self.boton_nueva.clicked.connect(self.crear_mapa)

    def cargar_mapa(self):
        self.senal_cargar_mapa.emit()
        self.hide()

    def crear_mapa(self):
        self.senal_crear_partida.emit()
        self.hide()




if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    ventana_inicio = VentanaInicio()

    ventana_inicio.show()
    sys.exit(a.exec())

