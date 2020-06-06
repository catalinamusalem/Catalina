import sys

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from time import perf_counter, clock, sleep



class VentanaPostRonda(QWidget):
    senal_nueva_ronda = pyqtSignal()
    senal_guardar_juego = pyqtSignal()
    senal_cerrar_juego = pyqtSignal()
    def __init__(self, *args):
        super().__init__(*args)
        self.ronda = str(0)
        self.reputacion = str(0)
        self.dinero = str(0)
        self.clientes_atendidos = str(0)
        self.clientes_no_atendidos = str(0)
        self.crear_pantalla()
        self.juego_perdido = False
        
        
    def datos(self,datos):
        self.n_ronda.setText(str(datos[0]))
        self.n_reputacion.setText(str(datos[1]))
        self.n_dinero.setText(str(datos[2]))
        self.n_atendidos.setText(str(datos[3]))
        self.n_perdidos.setText(str(datos[4]))
        self.show()
        if datos[1]== 0:
            self.label_terminar_partida.setText("DCCAFÉ HA SIDO CLAUSURADO :(")
            self.juego_perdido = True
            self.senal_cerrar_juego.emit()

    def crear_pantalla(self):
        self.setWindowTitle("Ventana Post Ronda")
        main_layout = QVBoxLayout()
        layout_datos = QVBoxLayout()
        layout_valores = QVBoxLayout()
        layout_arriba = QHBoxLayout()
        layout_central = QHBoxLayout()
        layout_botones = QHBoxLayout()
        self.resumen  = QLabel("RESUMEN RONDA N°", self)
        self.n_ronda = QLabel(self.ronda, self)
        self.perdidos = QLabel("CLIENTES PERDIDOS", self)
        self.n_perdidos = QLabel(self.clientes_no_atendidos, self)
        self.atendidos = QLabel("CLIENTES ATENDIDOS", self)
        self.n_atendidos = QLabel(self.clientes_atendidos, self)
        self.dinero_acumulado = QLabel("DINERO ACUMULADO", self)
        self. n_dinero = QLabel(self.dinero, self)
        self.label_reputacion = QLabel("REPUTACION", self)
        self.n_reputacion = QLabel(self.reputacion, self)
        self.label_terminar_partida = QLabel("         ", self)
        ###Botones
        self.boton_salir = QPushButton("SALIR", self)
        self.boton_guardar = QPushButton("GUARDAR", self)
        self.boton_continuar = QPushButton("CONTINUAR", self)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_guardar.clicked.connect(self.guardar)
        self.boton_continuar.clicked.connect(self.continuar)

        layout_arriba.addWidget(self.resumen)
        layout_arriba.addWidget(self.n_ronda)
        layout_datos.addWidget(self.perdidos)
        layout_datos.addWidget(self.atendidos)
        layout_datos.addWidget(self.dinero_acumulado)
        layout_datos.addWidget(self.label_reputacion)
        layout_valores.addWidget(self.n_perdidos)
        layout_valores.addWidget(self.n_atendidos)
        layout_valores.addWidget(self.n_dinero)
        layout_valores.addWidget(self.n_reputacion)
        layout_central.addLayout(layout_datos)
        layout_central.addLayout(layout_valores)
        layout_botones.addWidget(self.boton_salir)
        layout_botones.addWidget(self.boton_guardar)
        layout_botones.addWidget(self.boton_continuar)
        main_layout.addLayout(layout_arriba)
        main_layout.addLayout(layout_central)
        main_layout.addWidget(self.label_terminar_partida)
        main_layout.addLayout(layout_botones)
        layout_arriba.setAlignment(Qt.AlignCenter)
        self.setLayout(main_layout)
    
    def salir(self):
        QApplication.quit()
    def guardar(self):
        if self.juego_perdido == False:
            self.senal_guardar_juego.emit()
    def continuar(self):
        if self.juego_perdido == False:
            self.senal_nueva_ronda.emit()
            self.hide()




        



if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    ventana_post_ronda = VentanaPostRonda()

    ventana_post_ronda.show()
    sys.exit(a.exec())