# LIBRARY
from collections import deque
import pygame

# CONSTANTS
BLACK = (0, 0, 0)
CIAN = (0, 255, 255)
BLANCO = (255, 255, 255)
RED = (255, 0, 0)


class Interfaz():
    def __init__(self, x_max=1280, y_max=600):
        pygame.init()
        # Screen
        self.screen = pygame.display.set_mode([x_max, y_max])
        # Fonts
        self.font13 = pygame.font.Font('freesansbold.ttf', 13)
        self.font35 = pygame.font.Font('freesansbold.ttf', 35)
        # Rellenar con Blanco
        self.screen.fill(BLANCO)
        self.alturas = [0, 0, 0, 0]
        self.temp = [0, 0, 0, 0]
        self.h_ref = [0, 0]
        self.razones = [0, 0]
        self.voltajes = [0, 0]
        self.mouse_pos = [0, 0]
        self.modo = "A"
        self.alerta = False
        self.graficos = GraficosInterfaz(self)

    def dibujar_estanque(self, x, y, delta1, delta2):
        pygame.draw.line(self.screen, BLACK, (x, y), (x + delta1, y), 4)
        pygame.draw.line(self.screen, BLACK, (x, y), (x, y + delta2), 4)
        pygame.draw.line(self.screen, BLACK, (x + delta1, y), (x + delta1, y + delta2), 4)
        pygame.draw.line(self.screen, BLACK, (x, y + delta2), (x + delta1, y + delta2), 4)

    def dibujar_todo(self):
        delta1 = 100
        delta2 = 150
        # Cuadros verdes claros
        pygame.draw.rect(self.screen, (201, 215, 154), pygame.Rect(50, 200, 150, 45))
        pygame.draw.rect(self.screen, (201, 215, 154), pygame.Rect(450, 200, 150, 45))

        # Cuadro rojo claro
        pygame.draw.rect(self.screen, (251, 215, 194), pygame.Rect(250, 425, 140, 45))

        # Cuadros morados claros
        pygame.draw.rect(self.screen, (201, 154, 215), pygame.Rect(200 - 150, 30, 140, 45))
        pygame.draw.rect(self.screen, (201, 154, 215), pygame.Rect(340 + delta1 + 10, 30, 140, 45))
        pygame.draw.rect(self.screen, (201, 154, 215), pygame.Rect(200 - 150, 250 + 105, 140, 45))
        pygame.draw.rect(self.screen, (201, 154, 215), pygame.Rect(350 + delta1, 355, 140, 45))

        self.screen.blit(self.font13.render('Tank 1', True, BLACK), (230, 257+delta2))
        self.screen.blit(self.font13.render('Tank 2', True, BLACK), (370, 257+delta2))
        self.screen.blit(self.font13.render('Tank 3', True, BLACK), (230, 37+delta2))
        self.screen.blit(self.font13.render('Tank 4', True, BLACK), (370, 37+delta2))

        self.dibujar_estanque(200, 250, delta1, delta2)
        self.dibujar_estanque(340, 250, delta1, delta2)
        self.dibujar_estanque(200, 30, delta1, delta2)
        self.dibujar_estanque(340, 30, delta1, delta2)

    def h_referencias(self):
        self.screen.blit(self.font13.render('ref: ' + str(round(self.h_ref[0], 2)),
                         True, (2, 25, 153)), (225, 310))
        self.screen.blit(self.font13.render('ref: ' + str(round(self.h_ref[1], 2)), True,
                         (2, 25, 153)), (365, 310))

    def dibujar_h_t(self):
        (h1, h2, h3, h4) = self.alturas
        (t1, t2, t3, t4) = self.temp
        delta1 = 100
        c = BLACK
        self.screen.blit(self.font13.render('Altura 1: '+str(round(h1, 2)), True, c), (55, 360))
        self.screen.blit(self.font13.render('Temperatura 1: '+str(round(t1, 2)), True, c),
                         (55, 250 + 5 + 20 + 105))
        self.screen.blit(self.font13.render('Altura 2: ' + str(round(h2, 2)), True, c),
                         (340 + delta1 + 10 + 5, 250 + 5 + 105))
        self.screen.blit(self.font13.render('Temperatura 2: ' + str(round(t2, 2)), True, c),
                         (340 + delta1 + 10 + 5, 250 + 5 + 20 + 105))
        self.screen.blit(self.font13.render('Altura 3: ' + str(round(h3, 2)), True, c),
                         (200 - 150 + 5, 30 + 5))
        self.screen.blit(self.font13.render('Temperatura 3: ' + str(round(t3, 2)), True, c),
                         (200 - 150 + 5, 30 + 5 + 20))
        self.screen.blit(self.font13.render('Altura 4: ' + str(round(h4, 2)), True, c),
                         (340 + delta1 + 10 + 5, 30 + 5))
        self.screen.blit(self.font13.render('Temperatura 4: ' + str(round(t4, 2)), True, c),
                         (340 + delta1 + 10 + 5, 30 + 5 + 20))

    def dibujar_r_v(self):
        (razon1, razon2) = self.razones
        (voltaje1, voltaje2) = self.voltajes
        font = self.font13
        c = BLACK
        self.screen.blit(font.render('Razón de Flujo 1: '+str(round(razon1, 2)), True, c),
                         (55, 205))
        self.screen.blit(font.render('Voltaje Válvula 1: '+str(round(voltaje1, 2)), True, c),
                         (55, 225))
        self.screen.blit(font.render('Razón de Flujo 2: '+str(round(razon2, 2)), True, c),
                         (455, 205))
        self.screen.blit(font.render('Voltaje Válvula 2: '+str(round(voltaje2, 2)), True, c),
                         (455, 225))

    def dibujar_modo(self):
        c = BLACK
        font = self.font13
        if(self.modo == 'A'):
            self.screen.blit(font.render('Modo: ' + 'Automático', True, c), (255, 430))
        elif(self.modo == 'M'):
            self.screen.blit(font.render('Modo: ' + 'Manual', True, c), (255, 430))

    def dibujar_alerta(self):
        if(self.alerta == 1):
            pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(0, 200, 640, 45))
            self.screen.blit(self.font35.render('ALERTA', True, (255, 0, 0)), (260, 208))

    def dibujar_agua(self):
        delta1 = 100
        delta2 = 150
        screen = self.screen
        c = CIAN
        delta3 = 3
        (h1, h2, h3, h4) = self.alturas
        # Tanque 1:
        pygame.draw.rect(screen, c, pygame.Rect(200 + delta3, 250 + delta3, 96, 146))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(200 + delta3, 250 + delta3, 96,
                         int(146 - h1 * (146/50))))
        # Tanque 2:
        pygame.draw.rect(screen, c, pygame.Rect(340 + delta3, 250 + delta3, 96, 146))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(340 + delta3, 250 + delta3, 96,
                         int(146 - h2 * (146/50))))
        # Tanque 3:
        pygame.draw.rect(screen, c, pygame.Rect(200 + delta3, 30 + delta3, 96, 146))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(200 + delta3, 30 + delta3, 96,
                         int(146 - h3 * (146/50))))
        # Tanque 4:
        pygame.draw.rect(screen, c, pygame.Rect(340 + delta3, 30 + delta3, 96, 146))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(340 + delta3, 30 + delta3, 96,
                         int(146 - h4 * (146/50))))

    def actualizar(self, info_evento):
        self.alerta = info_evento[0]
        self.screen.fill(BLANCO)
        self.dibujar_todo()
        self.dibujar_h_t()
        self.dibujar_r_v()
        self.dibujar_modo()
        if self.alerta:
            self.dibujar_alerta()
            print()
        self.dibujar_agua()
        if self.modo == "A":
            self.h_referencias()
        self.graficos.actualizar()
        pygame.display.flip()

    def setear_variables(self, alturas, temp, razones, valvulas):
        self.alturas = alturas
        self.temp = temp
        self.razones = razones
        self.voltajes = valvulas
        self.graficos.actualizar_muestras(alturas)


class GraficosInterfaz():
    def __init__(self, interfaz: Interfaz):
        self.screen = interfaz.screen
        self.res_x = 200
        self.res_y = 200
        # [Tanq1, Tanq2, Tanq3, Tanq4]
        self.origenes = [(700, 550), (1020, 550), (700, 250), (1020, 250)]
        self.len_muestras = 19
        self.muestras = [deque([0 for i in range(self.len_muestras)]) for y in range(4)]

    def dibujar_cartesianas(self):
        for origen in self.origenes:
            origen_arriba = (origen[0], origen[1]-self.res_y)
            origen_derecha = (origen[0]+self.res_x, origen[1])
            pygame.draw.line(self.screen, BLACK, origen, origen_arriba, 4)
            pygame.draw.line(self.screen, BLACK, origen, origen_derecha, 4)

    def dibujar_muestras(self):
        for y in range(len(self.origenes)):
            origen = self.origenes[y]
            muestras = self.muestras[y]
            for x in range(len(muestras)):
                altura = muestras[x]
                pygame.draw.circle(self.screen, RED,
                                   (origen[0] + 10*x+10, origen[1] - (18*altura/5 + 20)), 4)

    def actualizar_muestras(self, alturas):
        for i in range(len(self.muestras)):
            lista = self.muestras[i]
            lista.rotate(-1)
            lista[-1] = alturas[i]

    def actualizar(self):
        self.dibujar_cartesianas()
        self.dibujar_muestras()


if __name__ == '__main__':
    pass
