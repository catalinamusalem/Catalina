from  PyQt5.QtWidgets import QApplication
import sys
from backend import Cliente
from frontend import VentanaInicio , SalaDeEspera

app = QApplication([])

PORT = 3245
HOST = 'localhost'


cliente = Cliente(PORT, HOST)
cliente.start()
ventanainicio = VentanaInicio()
ventanainicio.senal_verificar_nombre.connect(cliente.nombre_usuario)
cliente.senal_usuario_verificado.connect(ventanainicio.resultado_usuario)
salaespera = SalaDeEspera()
cliente.senal_sala_de_espera.connect(salaespera.jugadores)


#cliente.send_username.connect(window.get_username)
#cliente.update_lobby_chat.connect(window.update_chat)
#cliente.send_init_info_to_chat()

#window.send_msg_signal.connect(cliente.recive_msg_from_lobby)


ventanainicio.show()
sys.exit(app.exec_())