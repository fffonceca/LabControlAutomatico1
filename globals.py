from interfaz import Interfaz
from control import Control


def initialize():
    global info_evento, interfaz, control
    info_evento = (False, 0)
    interfaz = Interfaz()
    control = Control()
