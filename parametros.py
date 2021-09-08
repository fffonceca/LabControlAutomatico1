# CONSTANTS
BLACK = (0, 0, 0)
CIAN = (0, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# REFRESH CONSTANTS
PERIODO_CONTROL = 1
PERIODO_INTERFAZ = 0.1
PERIODO_GRAFICOS = 1

# RAM inicial
CANTIDAD_RAM = 1000

# Parametros iniciales de controlador
#             [[Kp1, Ki1, Kd1], [Kp2, Ki2, Kd2],  [Kp3, Ki3, Kd3], [Kp4, Ki4, Kd4]]
PID_INICIAL = [[0,   0,   0],   [0.1, 0.01, 0.02], [0.1, 0.01, 0.02], [0, 0, 0]]
