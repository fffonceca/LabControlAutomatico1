from util import BufferCircular
from interfaz import Interfaz
from control import Control
from parametros import CANTIDAD_RAM


def initialize():
    global info_evento, interfaz, control, buffer, correr_control
    info_evento = (False, 0)
    correr_control = False
    interfaz = Interfaz()
    control = Control()
    buffer = BufferCircular(CANTIDAD_RAM)
