from Libreria.cliente import Cliente
from pygame.locals import *
from util import obtener, eventos, funcion_handler
from interfaz import Interfaz
from control import Control
import threading


info_evento = (False, 0)


class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    data_change and event methods are called directly from receiving thread.
    Do not do expensive, slow or network operation there. Create another
    thread if you need to do such a thing
    """
    def datachange_notification(self, node, val, data):
        thread_handler = threading.Thread(target=funcion_handler, args=(node, val))
        thread_handler.start()

    # Eventos!!
    def event_notification(self, event):
        global info_evento
        info_evento = (True, event)


if __name__ == '__main__':
    cliente = Cliente("opc.tcp://localhost:4840/freeopcua/server/", suscribir_eventos=True,
                      SubHandler=SubHandler)
    cliente.conectar()
    interfaz = Interfaz()
    control = Control()
    while True:
        obtener(cliente, interfaz, control)
        eventos(interfaz, control)
        control.actualizar(cliente, interfaz)
        interfaz.actualizar(info_evento)
        info_evento = (False, 0)
