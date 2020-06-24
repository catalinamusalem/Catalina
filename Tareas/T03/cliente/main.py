from  PyQt5.QtWidgets import QApplication
import sys
from backend import BackEnd
from cliente import Cliente
from frontend import VentanaInicio , SalaDeEspera

app = QApplication([])

PORT = 3245
HOST = 'localhost'


cliente = Cliente(PORT, HOST)
backend = BackEnd()
cliente.start()
ventanainicio = VentanaInicio()
ventanainicio.senal_verificar_nombre.connect(backend.nombre_usuario)
backend.senal_usuario_verificado.connect(ventanainicio.resultado_usuario)
salaespera = SalaDeEspera()
backend.senal_sala_de_espera.connect(salaespera.jugadores)
cliente.senal_recibir_mensaje.connect(backend.recibir_mensaje)
backend.senal_enviar_mensaje_servidor.connect(cliente.send)



ventanainicio.show()
sys.exit(app.exec_())