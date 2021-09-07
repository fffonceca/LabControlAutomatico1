import threading
from Libreria.cliente import Cliente
from handler import SubHandler as SubHandlerExp
from pygame.locals import *
from util import obtener, eventos
import globals


def thread_programa(cliente):
    globals.interfaz.init_interfaz()
    while True:
        eventos(globals.interfaz, globals.control)
        globals.control.actualizar(cliente, globals.interfaz)
        globals.interfaz.actualizar(globals.info_evento)
        globals.info_evento = (False, 0)


if __name__ == '__main__':
    globals.initialize()
    cliente = Cliente("opc.tcp://localhost:4840/freeopcua/server/", suscribir_eventos=True,
                      SubHandler=SubHandlerExp)
    cliente.conectar()
    hilo = threading.Thread(target=thread_programa, args=(cliente,))
    hilo.start()
    obtener(cliente, globals.interfaz, globals.control)
    cliente.subscribir_cv()
    cliente.subscribir_mv()
