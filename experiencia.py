from Libreria.cliente import Cliente
from handler import SubHandler as SubHandlerExp
from util import obtener, eventos
import globals
import time
import threading


def thread_programa():
    globals.interfaz.init_interfaz()
    while True:
        eventos(globals.interfaz, globals.control)
        globals.interfaz.actualizar(globals.info_evento)
        globals.info_evento = (False, 0)
        time.sleep(1)


def thread_control(cliente):
    while True:
        globals.control.actualizar(cliente, globals.interfaz)
        time.sleep(1)


if __name__ == '__main__':
    globals.initialize()
    cliente = Cliente("opc.tcp://localhost:4840/freeopcua/server/", suscribir_eventos=True,
                      SubHandler=SubHandlerExp)
    cliente.conectar()
    hilo = threading.Thread(target=thread_programa)
    hilo_control = threading.Thread(target=thread_control, args=(cliente,))
    hilo.start()
    hilo_control.start()
    obtener(cliente, globals.interfaz, globals.control)
    cliente.subscribir_cv()
    cliente.subscribir_mv()
