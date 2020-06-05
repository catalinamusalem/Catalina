import sys

from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QTimer, QMimeData, QObject
from PyQt5.QtGui import QPixmap, QDrag, QPainter, QCursor
from PyQt5.QtWidgets import QApplication
from time import perf_counter, sleep
from threading import Thread, Event, Timer
import entidades
import entidades2
import p

class MisSenales(QObject):
    senal_crear_objeto = pyqtSignal(str,str)
class DragLabel(QLabel):
    def __init__(self,parent,image, objeto):
        super(QLabel,self).__init__(parent)
        self.setPixmap(QPixmap(image))    
        self.objeto = objeto
        self.show()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
 
    def mouseMoveEvent(self, event):
        if not(event.buttons() & Qt.LeftButton):
            return
        else:
            drag = QDrag(self)
            mimedata = QMimeData()
            mimedata.setText(self.objeto)
            mimedata.setImageData(self.pixmap().toImage())
            drag.setMimeData(mimedata)
            pixmap = QPixmap(self.size()) 
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)
 
class DropLabel(QLabel):
    
    def __init__(self, parent, senal_crear_objeto):
        super(QLabel,self).__init__(parent)
        self.senal_crear_objeto = senal_crear_objeto
        largo = p.LIMITE_X_SUP - p.LIMITE_X_INF
        ancho = p.LIMITE_Y_SUP - p.LIMITE_Y_INF
        self.setGeometry(p.LIMITE_X_INF, p.LIMITE_Y_INF, largo, ancho) 
        self.show()
        self.setAcceptDrops(True)
        self.posicion = p.POSICION_INICIAL
 
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.acceptProposedAction()
 
    def dropEvent(self, event):
        if event.mimeData().hasImage():
            self.posicion = event.pos()
            self.senal_crear_objeto.emit(str(event.pos()),event.mimeData().text())

class VentanaPrincipal(QWidget):
    senal_tecla_presionada = pyqtSignal(str,list)
    senal_comenzar_juego = pyqtSignal()
    senal_parar_juego = pyqtSignal(bool)
    senal_nueva_ronda = pyqtSignal()
    senal_cliente_creado = pyqtSignal(entidades.Clientes)
    senal_cargar_entidades = pyqtSignal(entidades2.Jugador, list, list)
    senal_agregar_bocadillo_mesa = pyqtSignal(entidades.Bocadillo)
    senal_nueva_ronda = pyqtSignal()
    senal_es_posible_poner_objeto = pyqtSignal(int, int, list, str)
    senal_cargar_mesa = pyqtSignal(entidades.Mesa)
    senal_forzar_terminar_ronda = pyqtSignal( )
    senal_cargar_cocina = pyqtSignal(entidades2.Chef)
    senal_aumentar_dinero = pyqtSignal()
    senal_aumentar_reputacion = pyqtSignal()
    senal_forzar_terminar_ronda = pyqtSignal()
    senal_eliminar_mesa = pyqtSignal(int, int)

    def __init__(self, *args):
        super().__init__(*args)
        self.crear_pantalla()
        self.pausar = 1
        self.comenzar = 0
        self.juego_en_curso = False
        self.presionada = [0,0,0]  #Teclas presionadas
        
    def recibir_señal(self,senal_crear_objeto):
        self.senal_crear_objeto = senal_crear_objeto
        self.senal_crear_objeto.connect(self.comprar_objeto)
        lbl_to_drop = DropLabel(self, senal_crear_objeto)
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
        self.n_reputacion = QLabel("0000", self)
        self.n_dinero = QLabel("0000", self)
        self.dinero.adjustSize()
        self.n_ronda = QLabel("0000", self)
        self.atendidos = QLabel("ATENDIDOS", self)
        self.perdidos = QLabel("PERDIDOS", self)
        self.proximos= QLabel("PRÓXIMOS", self)
        self.n_atendidos = QLabel("0000",self)
        self.n_perdidos = QLabel("0000",self)
        self.n_proximos = QLabel("0000",self)
        #Botones
        self.boton_pausar = QPushButton("PAUSAR",self)
        self.boton_pausar.clicked.connect(self.pausar_)
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
        self.cocina = DragLabel(self,p.RUTA_COCINA, "chef")
        self.cocina.setGeometry(2800, 500, 300, 300)
        self.cocina.setScaledContents(True)
        self.mesa = DragLabel(self, p.RUTA_MESA, "mesa")
        self.mesa.setGeometry(2870, 900, 150, 150)
        self.mesa.setScaledContents(True)
        self.precio_cocina = QLabel(f"$ {str(p.PRECIO_COCINA)}", self)
        self.precio_mesa = QLabel(f"$ {str(p.PRECIO_MESA)}", self)
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
        
        self.tienda.move(2850,360)
        self.precio_cocina.move(2900,800)
        self.precio_mesa.move(2900,1100)

        self.mesas = []
        self.cocinas = []
        self.mesero = QLabel(self)
        self.cliente = QLabel(self)
        self.bocadillos = []
    
        
    def comprar_objeto(self, posicion, tipo):
        if self.juego_en_curso == False:
            posicion1 = str(posicion)[20:-1]
            posicion2 = posicion1.split(",")
            self.posicion_objeto_comprado = posicion2
            x = int(posicion2[0])+ p.LIMITE_X_INF
            y = int(posicion2[1])+ p.LIMITE_Y_INF
            if tipo == "mesa":
                self.senal_es_posible_poner_objeto.emit(x, y, [p.LARGO_MESA, p.ANCHO_MESA], tipo)
            if tipo == "chef":
                self.senal_es_posible_poner_objeto.emit(x, y,[p.LARGO_COCINA, p.ANCHO_COCINA],tipo)
    
    def comprar_objeto_posible(self,resultado, tipo):
        if resultado == "True":
            x = int(self.posicion_objeto_comprado[0]) + p.LIMITE_X_INF
            y = int(self.posicion_objeto_comprado[1]) + p.LIMITE_Y_INF
            if tipo == "mesa":
                self.mesa = entidades.Mesa(self)
                self.mesa.move(x, y)
                pixeles_mesa = QPixmap(p.RUTA_MESA)
                self.mesa.setPixmap(pixeles_mesa.scaled(p.LARGO_MESA,p.ANCHO_MESA))
                self.mesa.posicion(x, y)
                self.mesas.append(self.mesa)
                self.mesa.show()
                self.senal_cargar_mesa.emit(self.mesa)
            if tipo == "chef":
                self.cocina = entidades2.Chef(self)
                self.cocina.move(x, y)
                pixeles_cocina = QPixmap(p.RUTA_COCINA)
                self.cocina.setPixmap(pixeles_cocina.scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
                self.cocinas.append(self.cocina)
                self.cocina.show()
                self.senal_cargar_cocina.emit(self.cocina)
    def cargar_juego(self, datos):
        for i in datos[0]:
            if i[0] == "mesa":
                self.dato = entidades.Mesa(self)
                self.dato.move(i[1],i[2])
                pixeles_dato = QPixmap(i[3])
                self.dato.setPixmap((pixeles_dato).scaled(p.LARGO_MESA,p.ANCHO_MESA))
                self.dato.posicion(i[1],i[2])
                self.mesas.append(self.dato)
            if i[0] == "chef":
                self.dato = entidades2.Chef(self)
                self.dato.move(i[1],i[2])
                pixeles_dato = QPixmap(i[3])
                self.dato.setPixmap((pixeles_dato).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
                self.cocinas.append(self.dato)
            if i[0] == "mesero":
                
                self.mesero = entidades2.Jugador(self)
                self.mesero.move(i[1],i[2])
                self.mesero.setPixmap((QPixmap(i[3])).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                
        
        self.senal_cargar_entidades.emit(self.mesero,self.mesas, self.cocinas)
        self.n_dinero.setText(str(datos[1][0][0]))
        self.n_reputacion.setText(str(datos[1][0][1]))
        self.n_ronda.setText(str(datos[1][0][2]))
        self.show()
    def keyPressEvent(self, event):
        
        posicion = str(self.mesero.pos())[20:-1]
        posicion_ = posicion.split(",")
        self.presionada.append(event.key())
        
        if self.juego_en_curso == True:
            tecla = self.presionada[-3]
            if event.key() == 87 or event.key() == 83 or event.key() == 65 or event.key() == 68:
                self.senal_tecla_presionada.emit(str(event.key()),posicion_)
                self.presionada = [0,0,0]
                
            if event.key() == 80:
                self.pausar_()
                self.presionada = [0,0,0]
                
            if tecla == 70 and self.presionada[-2] == 73 and self.presionada[-1] == 78:
                self.presionada = [0,0,0]
                self.juego_en_curso = False
                self.senal_forzar_terminar_ronda.emit()
        if self.presionada[-3] == 77 and self.presionada[-2] == 79 and self.presionada[-1] == 78:
            self.presionada = [0,0,0]
            
            self.senal_aumentar_dinero.emit()
        if self.presionada[-3] == 82 and self.presionada[-2] == 84 and self.presionada[-1] == 71:
            self.presionada = [0,0,0]
            self.senal_aumentar_reputacion.emit()
        
    def mousePressEvent(self, event):
        if self.juego_en_curso == False:
            self.senal_eliminar_mesa.emit(event.x(), event.y())
        
    def mover_jugador(self,posible, direccion):
        if self.juego_en_curso == True:
            if self.pausar%2 == 1:
                if posible  == True:
                    self.mesero.avanzar(direccion)
                if posible == False:
                    self.mesero.movimiento_en_falso(direccion)
    def llegada_clientes(self):
        self.cliente = entidades.Clientes(self)
        self.clientes.append(self.cliente)
        self.senal_cliente_creado.emit(self.cliente)

    def creacion_bocadillo(self):
        self.bocadillo = entidades.Bocadillo(self)
        self.bocadillos.append(self.bocadillo)
        self.senal_agregar_bocadillo_mesa.emit(self.bocadillo)
        
    def comenzar_juego(self):
        self.clientes = []
        if self.juego_en_curso == False:
            if self.comenzar == 0:
                self.senal_comenzar_juego.emit()
                self.comenzar += 1
            else:
                self.senal_nueva_ronda.emit()
            self.juego_en_curso = True
    def actualizar_estadisticas(self,datos):
        self.n_reputacion.setText(str(datos[0]))
        self.n_dinero.setText(str(datos[1]))
        self.n_dinero.adjustSize()
        self.n_ronda.setText(str(datos[2]))
        self.n_atendidos.setText(str(datos[3]))
        self.n_perdidos.setText(str(datos[4]))
        self.n_proximos.setText(str(datos[5]))
    
    def salir(self):
        QApplication.quit()
    def pausar_(self):
        if self.juego_en_curso == True:
            if self.pausar%2 == 1:
                self.boton_pausar.setText("CONTINUAR")
                self.senal_parar_juego.emit(True)
            else:
                self.boton_pausar.setText("PAUSAR")
                self.senal_parar_juego.emit(False)
            self.pausar += 1

    def terminar_ronda(self):
        self.juego_en_curso = False

    
    
    
     
if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)
    senales = MisSenales()
    ventana_principal = VentanaPrincipal()
    ventana_principal.recibir_señal(senales.senal_crear_objeto)

    ventana_principal.show()
    sys.exit(a.exec())







