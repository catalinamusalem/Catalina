from  PyQt5.QtWidgets import QApplication
import sys
from backend import BackEnd
from cliente import Cliente
from frontend import VentanaInicio , SalaDeEspera, VentanaPrincipal, ElegirColor
import json
with open("parametros.json") as f:
    data = json.load(f)
app = QApplication([])
PORT = data["port"]
HOST = data["host"]



cliente = Cliente(PORT, HOST)
backend = BackEnd()
cliente.start()
ventanainicio = VentanaInicio()
ventanainicio.senal_verificar_nombre.connect(backend.nombre_usuario)
backend.senal_usuario_verificado.connect(ventanainicio.resultado_usuario)
salaespera = SalaDeEspera()
ventanaprincipal = VentanaPrincipal()
elegircolor = ElegirColor()
backend.senal_sala_de_espera.connect(salaespera.jugadores)
cliente.senal_recibir_mensaje.connect(backend.recibir_mensaje)
backend.senal_enviar_mensaje_servidor.connect(cliente.send)
backend.senal_empezar_partida.connect(salaespera.empezar_partida)
backend.senal_empezar_partida_vp.connect(ventanaprincipal.empezar_partida)
backend.senal_enviar_carta_reverso.connect(ventanaprincipal.recibir_carta_reverso)
backend.senal_enviar_carta_mano.connect(ventanaprincipal.recibir_carta_mano)
backend.senal_enviar_carta_pozo.connect(ventanaprincipal.recibir_carta_pozo)
backend.senal_cartas_jugadores.connect(ventanaprincipal.cartas_jugadores)
backend.senal_cambiar_turno.connect(ventanaprincipal.recibir_turno)
ventanaprincipal.senal_jugar_carta.connect(backend.jugar_carta)
backend.senal_carta_jugada.connect(ventanaprincipal.carta_jugada)
ventanaprincipal.senal_robar_carta.connect(backend.robar_carta)
ventanaprincipal.senal_gritar_dcc4.connect(backend.gritar_dcc4)
ventanaprincipal.senal_elegir_color.connect(elegircolor.mostrar) ####
elegircolor.senal_cambiar_color.connect(backend.color)
backend.senal_actualizar_color.connect(ventanaprincipal.color_elegido)
ventanainicio.show()
sys.exit(app.exec_()) 