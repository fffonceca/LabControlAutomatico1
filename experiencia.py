from Libreria.cliente import Cliente
from handler import SubHandler as SubHandlerExp
from pygame.locals import *
from util import obtener, eventos
from interfaz import Interfaz
from control import Control
import globals


if __name__ == '__main__':
    globals.initialize()
    cliente = Cliente("opc.tcp://localhost:4840/freeopcua/server/", suscribir_eventos=True,
                      SubHandler=SubHandlerExp)
    cliente.conectar()
    cliente.subscribir_cv()
    cliente.subscribir_mv()
    interfaz = Interfaz()
    control = Control()
    while True:
        obtener(cliente, interfaz, control)
        eventos(interfaz, control)
        control.actualizar(cliente, interfaz)
        interfaz.actualizar(globals.info_evento)
        globals.info_evento = (False, 0)
