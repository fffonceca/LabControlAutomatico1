from Libreria.cliente import Cliente
from handler import SubHandler as SubHandlerExp
from util import obtener, eventos
import parametros
import time
import threading
import globals


def thread_interfaz(cliente):
    globals.interfaz.init_interfaz()
    obtener(cliente, globals.interfaz, globals.control)
    i = 0
    while True:
        eventos(globals.interfaz, globals.control)
        if i % (parametros.PERIODO_GRAFICOS//parametros.PERIODO_INTERFAZ) == 0:
            globals.interfaz.graficos.actualizar_muestras(globals.interfaz.alturas,
                                                          globals.interfaz.voltajes)
        globals.interfaz.actualizar(globals.info_evento)
        globals.info_evento = (False, 0)
        time.sleep(parametros.PERIODO_INTERFAZ)
        i += 1


def thread_control(cliente):
    while True:
        globals.control.actualizar(cliente, globals.interfaz)
        time.sleep(parametros.PERIODO_CONTROL)


if __name__ == '__main__':
    globals.initialize()
    cliente = Cliente("opc.tcp://localhost:4840/freeopcua/server/", suscribir_eventos=True,
                      SubHandler=SubHandlerExp)
    cliente.conectar()
    hilo = threading.Thread(target=thread_interfaz, args=[cliente])
    hilo_control = threading.Thread(target=thread_control, args=[cliente])
    hilo.start()
    hilo_control.start()
    cliente.subscribir_cv()
    cliente.subscribir_mv()
    while True:
        pass
