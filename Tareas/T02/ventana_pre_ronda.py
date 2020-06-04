import sys

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from time import perf_counter, sleep
from threading import Thread, Event
import entidades
import p

class VentanaJuego(QWidget):
    senal_tecla_presionada = pyqtSignal(str,list)
    senal_comenzar_juego = pyqtSignal()
    senal_parar_juego = pyqtSignal(bool)
    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()
        self.pausar = 1  
        self.comenzar = 0 #Para que solo se pueda apretar comenzar juego una vez 
 
    def crear_pantalla(self):
        #Logo
        self.logo_inicio=QLabel(self)
        pixeles_logo = QPixmap(p.RUTA_LOGO_INICIO).scaled(800,300,Qt.KeepAspectRatio)
        self.logo_inicio.setPixmap(pixeles_logo)
        self.logo_inicio.move(0,0)
        #Datos
        self.reputacion  = QLabel("REPUTACIÓN", self)
        self.dinero = QLabel("DINERO", self)
        self.ronda = QLabel("RONDA N°", self)
        self.n_reputacion = QLabel("0", self)
        self.n_dinero = QLabel("0", self)
        self.n_ronda = QLabel("1", self)
        self.atendidos = QLabel("ATENDIDOS", self)
        self.perdidos = QLabel("PERDIDOS", self)
        self.proximos= QLabel("PRÓXIMOS", self)
        self.n_atendidos = QLabel("0",self)
        self.n_perdidos = QLabel("0",self)
        self.n_proximos = QLabel("0",self)
        #Botones
        self.boton_pausar = QPushButton("PAUSAR",self)
        self.boton_pausar.clicked.connect(self.pausar)
        self.boton_salir = QPushButton("SALIR",self)
        self.boton_salir.clicked.connect(self.salir)
        self.boton_comenzar = QPushButton("COMENZAR",self)
        self.boton_comenzar.clicked.connect(self.comenzar_juego)
        #Mapa
        self.mapa=QLabel(self)
        self.mapa.setGeometry(0, 360, p.LARGO_MAPA, p.ANCHO_MAPA)
        pixeles_mapa = QPixmap(p.RUTA_MAPA)
        self.mapa.setPixmap(pixeles_mapa)
        self.mapa.setScaledContents(True)
        #Tienda
        self.tienda = QLabel("----TIENDA----", self)
        self.cocina = QLabel(self)
        self.cocina.setGeometry(2800, 500, 300, 300)
        pixeles_cocina = QPixmap(p.RUTA_COCINA)
        self.cocina.setPixmap(pixeles_cocina)
        self.cocina.setScaledContents(True)
        self.mesa = QLabel(self)
        self.mesa.setGeometry(2870, 900, 150, 150)
        pixeles_mesa = QPixmap(p.RUTA_MESA)
    
        self.mesa.setPixmap(pixeles_mesa)
        self.mesa.setScaledContents(True)
        self.precio_cocina = QLabel("$", self)
        self.precio_mesa = QLabel("$", self)
        #Ubicaciones
        self.reputacion.move(850,50)
        self.dinero.move(850,150) 
        self.ronda.move(850,250) 
        self.n_reputacion.move(1050,50)
        self.n_dinero.move(1050,150)
        self.n_ronda.move(1050,250)
        self.atendidos.move(1550,50)
        self.perdidos.move(1550,150)
        self.proximos.move(1550,250)
        self.n_atendidos.move(1750,50)
        self.n_perdidos.move(1750,150)
        self.n_proximos.move(1750,250)
        self.boton_pausar.move(2000,100) 
        self.boton_salir.move(2000,200)
        self.boton_comenzar.move(1150,240)
        
        self.tienda.move(2900,360)
        self.precio_cocina.move(2900,800)
        self.precio_mesa.move(2900,1100)

        self.mesas = []
        self.cocinas = []
        self.mesero = QLabel(self)
        
    
    def cargar_juego(self, datos):
        for i in datos[0]:
            self.dato = QLabel(self)
            self.dato.move(i[1],i[2])
            pixeles_dato = QPixmap(i[3])
            if i[0] == "mesa":
                self.dato.setPixmap((pixeles_dato).scaled(p.LARGO_MESA,p.ANCHO_MESA))
                self.mesas.append(self.dato)
            if i[0] == "chef":
                self.dato.setPixmap((pixeles_dato).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
                self.cocinas.append(self.dato)
            if i[0] == "mesero":
                self.mesero = entidades.Jugador(self)
                self.mesero.move(i[1],i[2])
                self.mesero.setPixmap((pixeles_dato).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                print(self.mesero.pos())
        
        self.n_dinero.setText(str(datos[1][0][0]))
        self.n_reputacion.setText(str(datos[1][0][1]))
        self.n_ronda.setText(str(datos[1][0][2]))
        
        #FALTAN PLATOS PREPARADOS CHEF 
            
        self.show()
    def keyPressEvent(self, event):
        posicion = str(self.mesero.pos())[20:-1]
        posicion_ = posicion.split(",")
        self.senal_tecla_presionada.emit(str(event.key()),posicion_)

    def mover_jugador(self,posible, direccion):
        if posible  == True:
            self.mesero.avanzar(direccion)
    def comenzar_juego(self):
        if self.comenzar == 0:
            self.senal_comenzar_juego.emit()
            self.comenzar += 1
        
    def salir(self):
        QApplication.quit()
    def pausar(self):
        if self.pausar%2 == 1:
            self.boton_pausar.setText("CONTINUAR")
            self.senal_parar_juego.emit(True)
        else:
            self.boton_pausar.setText("PAUSAR")
            self.senal_parar_juego.emit(False)
        self.pausar += 1

     #def comprar_tienda(self):
        
       
        
        
#class DragAndDrop(QLineEdit):
    #def __init__(self):
     #   super().__init__()
      #  self.setAcceptDrops(True)
    #def dragEnterEvent(self, event):
     #   if event.QmimeData().hasImage:
      #      event.accept()
       # else:
        #    ignore()
    #def dropEvent(self,event)
     #   print("drop event")

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    ventana_pre_ronda = VentanaPreRonda()

    ventana_pre_ronda.show()
    sys.exit(a.exec())







