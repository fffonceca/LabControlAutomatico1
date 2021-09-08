from handler import SubHandler as SubHandlerExp
from Libreria.cliente import Cliente
from util import obtener, eventos
import parametros
import time
import threading
import globals


def thread_interfaz(cliente):
    globals.interfaz.init_interfaz()
    obtener(cliente, globals.interfaz, globals.control)
    globals.correr_control = True
    i = 0
    while True:
        eventos(globals.interfaz, globals.control, globals.buffer)
        if i % (parametros.PERIODO_GRAFICOS//parametros.PERIODO_INTERFAZ) == 0:
            globals.interfaz.graficos.actualizar_muestras(globals.interfaz.alturas,
                                                          globals.interfaz.voltajes)
        globals.interfaz.actualizar(globals.info_evento, globals.control)
        globals.info_evento = (False, 0)
        time.sleep(parametros.PERIODO_INTERFAZ)
        i += 1


def thread_control(cliente):
    while not globals.correr_control:
        print("Control: Esperando datos iniciales...")
        time.sleep(parametros.PERIODO_CONTROL)
    while True:
        globals.control.actualizar(cliente, globals.interfaz)
        globals.buffer.insertar_dato(globals.interfaz, globals.control)
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
