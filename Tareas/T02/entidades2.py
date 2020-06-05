import sys
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from random import random
import p
from threading import Thread, current_thread, Event, Timer
from time import sleep
from math import floor

class Jugador(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self._lleva_comida = False
        self.__sprite = 0

    @property
    def sprite(self):
        return self.__sprite
    @sprite.setter
    def sprite(self, p):
        self.__sprite = p
    @property
    def lleva_comida(self):
        return self._lleva_comida
    @lleva_comida.setter
    def lleva_comida(self, p):
        self._lleva_comida = p
        
    def cambiar_sprite(self, direccion):
        if self.lleva_comida == False:
            if direccion == "83":
                if self.sprite == 1:
                    self.setPixmap((QPixmap(p.MSRO_ABAJO_1)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    self.setPixmap((QPixmap(p.MSRO_ABAJO_2)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    self.setPixmap((QPixmap(p.MSRO_ABAJO_3)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    self.setPixmap((QPixmap(p.MSRO_ABAJO_2)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
                    
            if direccion == "87":
                if self.sprite == 1:
                    pixeles = QPixmap(p.MSRO_ARRIBA_1)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    pixeles = QPixmap(p.MSRO_ARRIBA_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    pixeles = QPixmap(p.MSRO_ARRIBA_3)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    pixeles = QPixmap(p.MSRO_ARRIBA_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
            if direccion == "65":
                if self.sprite == 1:
                    self.setPixmap((QPixmap(p.MSRO_IZQ_1)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    self.setPixmap((QPixmap(p.MSRO_IZQ_2)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    self.setPixmap((QPixmap(p.MSRO_IZQ_3)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    self.setPixmap((QPixmap(p.MSRO_IZQ_2)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
                
            if direccion == "68":
                if self.sprite == 1:
                    self.setPixmap((QPixmap(p.MSRO_DER_1)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    self.setPixmap((QPixmap(p.MSRO_DER_2)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    self.setPixmap((QPixmap(p.MSRO_DER_3)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    self.setPixmap((QPixmap(p.MSRO_DER_2)).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
        if self.lleva_comida == True:
            if direccion == "83":
                if self.sprite == 1:
                    pixeles = QPixmap(p.MSRO_ABAJO_SNACK_1)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    pixeles = QPixmap(p.MSRO_ABAJO_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    pixeles = QPixmap(p.MSRO_ABAJO_SNACK_3)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    pixeles = QPixmap(p.MSRO_ABAJO_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
                    
            if direccion == "87":
                if self.sprite == 1:
                    pixeles = QPixmap(p.MSRO_ARRIBA_SNACK_1)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    pixeles = QPixmap(p.MSRO_ARRIBA_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    pixeles = QPixmap(p.MSRO_ARRIBA_SNACK_3)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    pixeles = QPixmap(p.MSRO_ARRIBA_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
            if direccion == "65":
                if self.sprite == 1:
                    pixeles = QPixmap(p.MSRO_IZQ_SNACK_1)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    pixeles = QPixmap(p.MSRO_IZQ_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    pixeles = QPixmap(p.MSRO_IZQ_SNACK_3)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    pixeles = QPixmap(p.MSRO_IZQ_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
                
            if direccion == "68":
                if self.sprite == 1:
                    pixeles = QPixmap(p.MSRO_DER_SNACK_1)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 2 :
                    pixeles = QPixmap(p.MSRO_DER_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                if self.sprite == 3:
                    pixeles = QPixmap(p.MSRO_DER_SNACK_3)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO)) 
                if self.sprite == 4 :
                    pixeles = QPixmap(p.MSRO_DER_SNACK_2)
                    self.setPixmap((pixeles).scaled(p.LARGO_MESERO,p.ANCHO_MESERO))
                    self.sprite -= 4
            
            
        
    def avanzar(self, direccion):
        
        if direccion == "83":
            self.move(self.pos().x(), self.pos().y() + p.VEL_MOVIMIENTO)
            self.sprite += 1
            self.cambiar_sprite(direccion)
            
        if direccion == "87":
            self.move(self.pos().x(), self.pos().y() - p.VEL_MOVIMIENTO)
            self.sprite += 1
            self.cambiar_sprite(direccion)
            
            
        if direccion == "65":
            self.move(self.pos().x() - p.VEL_MOVIMIENTO, self.pos().y())
            self.sprite += 1
            self.cambiar_sprite(direccion)
            
        if direccion == "68":
            self.move(self.pos().x() + p.VEL_MOVIMIENTO, self.pos().y() )
            self.sprite += 1
            self.cambiar_sprite(direccion)
    def movimiento_en_falso(self,direccion):
        if direccion == "83":
            
            self.sprite += 1
            self.cambiar_sprite(direccion)
            
        if direccion == "87":
            
            self.sprite += 1
            self.cambiar_sprite(direccion)
            
            
        if direccion == "65":
            
            self.sprite += 1
            self.cambiar_sprite(direccion)
            
        if direccion == "68":
            
            self.sprite += 1
            self.cambiar_sprite(direccion)

    def entregar_comida(self):
        return self.lleva_comida 
    def retirar_comida(self, nivel_chef):
        self.lleva_comida = True
        self.nivel_chef = nivel_chef
    def comida_entregada(self):
        self.lleva_comida = False
    

class Chef(QLabel):
    def __init__(self, *args):
        super().__init__(*args)
        self.nivel = 1
        self.cocinando = False
        self.plato_listo = False
        self.numero_sprite = 1
        self.platos_preparados = 0
        self.reputacion = 0
        self.tiempo_preparacion = 0
        self.pausa= 1
    def equivocarse(self):
        probabilidad = 0.3/(self.nivel + 1)
        numero = random()
        if numero < probabilidad:
            return True
        else:
            return False
    def tiempo_de_preparacion(self, reputacion):  # pedido por entidad bocadillo 
        self.reputacion = reputacion
        self.tiempo_preparacion =  max(0, 15 - reputacion - self.nivel * 2)
    def choque(self,mesero):

        if  self.cocinando == False and self.plato_listo == False:
            self.empezar_a_cocinar(self.tiempo_preparacion)
        if mesero.entregar_comida()==False and self.cocinando== False and self.plato_listo == True:
            mesero.retirar_comida(self.nivel)
            self.plato_listo = False
            self.setPixmap((QPixmap(p.RUTA_COCINA)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
            

    def empezar_a_cocinar(self,tiempo_preparacion):
        self.cocinar = QTimer()
        self.cocinar.setInterval((tiempo_preparacion/15) *(1/p.VELOCIDAD_RELOJ) * 1000)
        self.cocinar.timeout.connect(self.cambiar_sprites)
        self.cocinar.start()
        self.cocinando = True
    def subir_nivel(self):
        
        if self.platos_preparados == p.PLATOS_INTERMEDIO:
            self.nivel = 2
            print("Nivel 2")
        if self.platos_preparados == p.PLATOS_EXPERTO:
            self.nivel = 3
            print("Nivel 3")
        self.tiempo_de_preparacion(self.reputacion)
        


    def cambiar_sprites(self):
        if self.numero_sprite == 1:
            self.setPixmap((QPixmap(p.RUTA_COCINA_1)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 2:
            self.setPixmap((QPixmap(p.RUTA_COCINA_2)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 3:
            self.setPixmap((QPixmap(p.RUTA_COCINA_3)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 4:
            self.setPixmap((QPixmap(p.RUTA_COCINA_4)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 5:
            self.setPixmap((QPixmap(p.RUTA_COCINA_5)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 6:
            self.setPixmap((QPixmap(p.RUTA_COCINA_6)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 7:
            self.setPixmap((QPixmap(p.RUTA_COCINA_7)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 8:
            self.setPixmap((QPixmap(p.RUTA_COCINA_8)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 9:
            self.setPixmap((QPixmap(p.RUTA_COCINA_9)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 10:
            self.setPixmap((QPixmap(p.RUTA_COCINA_10)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 11:
            self.setPixmap((QPixmap(p.RUTA_COCINA_11)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 12:
            self.setPixmap((QPixmap(p.RUTA_COCINA_12)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 13:
            self.setPixmap((QPixmap(p.RUTA_COCINA_13)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        if self.numero_sprite == 14:
            self.setPixmap((QPixmap(p.RUTA_COCINA_14)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        

        if self.numero_sprite == 15:
            if self.equivocarse() == False:
                self.setPixmap((QPixmap(p.RUTA_COCINA_15)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA)) 
                self.plato_listo = True 
                self.platos_preparados += 1
                print(self.platos_preparados)
                platos = self.platos_preparados
                if platos == p.PLATOS_INTERMEDIO or platos == p.PLATOS_EXPERTO:
                    self.subir_nivel()
            else:
                 self.setPixmap((QPixmap(p.RUTA_COCINA)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
                 self.plato_listo = False
            self.numero_sprite = 0
            
            self.cocinar.stop()
            self.cocinando = False
        self.numero_sprite +=  1

    def terminar_ronda(self):
        if self.cocinando == True:
            self.cocinar.stop()
        self.numero_sprite = 1
        self.setPixmap((QPixmap(p.RUTA_COCINA)).scaled(p.LARGO_COCINA,p.ANCHO_COCINA))
        self.plato_listo = False
        self.cocinando = False
    
    def pausar(self):
        if self.pausa == 1:
            if self.cocinando == True:
                self.cocinar.stop()
            self.pausa += 1
        else:
            if self.cocinando == True:
                self.cocinar.start()
            self.pausa -= 1
    def desaparecer(self):
        self.setPixmap(QPixmap())