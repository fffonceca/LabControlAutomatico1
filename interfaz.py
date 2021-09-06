# LIBRARY
from collections import deque
import pygame

# CONSTANTS
BLACK = (0, 0, 0)
CIAN = (0, 255, 255)
BLANCO = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Interfaz():
    def __init__(self, x_max=1280, y_max=600):
        pygame.init()
        # Screen
        self.x_max = x_max
        self.y_max = y_max
        self.screen = pygame.display.set_mode([x_max, y_max])
        # Fonts
        self.font13 = pygame.font.Font('freesansbold.ttf', 13)
        self.font35 = pygame.font.Font('freesansbold.ttf', 35)
        # Rellenar con Blanco
        self.screen.fill(BLANCO)
        self.alturas = [0, 0, 0, 0]
        self.temp = [0, 0, 0, 0]
        self.h_ref = [25, 25]
        self.razones = [0, 0]
        self.voltajes = [0, 0]
        self.modo = "A"
        self.alerta = False
        self.graficos = GraficosInterfaz(self)
        self.constantes = ConstantesInterfaz(self)

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
        pygame.draw.rect(self.screen, (251, 215, 194), pygame.Rect(250, 430, 140, 35))  # 425, 45

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
        pygame.draw.line(self.screen, (0, 0, 0),
                         (200, self.h_ref[0]*(-146/50)+399),
                         (300, self.h_ref[0]*(-146/50)+399), 2)
        pygame.draw.line(self.screen, (0, 0, 0),
                         (340, self.h_ref[1]*(-146/50)+399),
                         (440, self.h_ref[1]*(-146/50)+399), 2)

    def dibujar_h_t(self):
        (h1, h2, h3, h4) = self.alturas
        (t1, t2, t3, t4) = self.temp
        delta1 = 100
        c = BLACK
        self.screen.blit(self.font13.render('Altura 1: '+str(round(h1, 2)) + ' cm', True, c),
                         (55, 360))
        self.screen.blit(self.font13.render('Temperatura 1: '+str(round(t1, 2)) + '°C', True, c),
                         (55, 250 + 5 + 20 + 105))
        self.screen.blit(self.font13.render('Altura 2: ' + str(round(h2, 2)) + ' cm', True, c),
                         (340 + delta1 + 10 + 5, 250 + 5 + 105))
        self.screen.blit(self.font13.render('Temperatura 2: ' + str(round(t2, 2)) + '°C', True, c),
                         (340 + delta1 + 10 + 5, 250 + 5 + 20 + 105))
        self.screen.blit(self.font13.render('Altura 3: ' + str(round(h3, 2)) + ' cm', True, c),
                         (200 - 150 + 5, 30 + 5))
        self.screen.blit(self.font13.render('Temperatura 3: ' + str(round(t3, 2)) + '°C', True, c),
                         (200 - 150 + 5, 30 + 5 + 20))
        self.screen.blit(self.font13.render('Altura 4: ' + str(round(h4, 2)) + ' cm', True, c),
                         (340 + delta1 + 10 + 5, 30 + 5))
        self.screen.blit(self.font13.render('Temperatura 4: ' + str(round(t4, 2)) + '°C', True, c),
                         (340 + delta1 + 10 + 5, 30 + 5 + 20))

    def dibujar_r_v(self):
        (razon1, razon2) = self.razones
        (voltaje1, voltaje2) = self.voltajes
        font = self.font13
        c = BLACK
        self.screen.blit(font.render('Razón de Flujo 1: '+str(round(razon1, 2)), True, c),
                         (55, 205))
        self.screen.blit(font.render('Voltaje Válvula 1: '+str(round(voltaje1, 2)) + ' V', True, c),
                         (55, 225))
        self.screen.blit(font.render('Razón de Flujo 2: '+str(round(razon2, 2)), True, c),
                         (455, 205))
        self.screen.blit(font.render('Voltaje Válvula 2: '+str(round(voltaje2, 2)) + ' V', True, c),
                         (455, 225))

    def dibujar_modo(self):
        c = BLACK
        font = self.font13
        if(self.modo == 'A'):
            self.screen.blit(font.render('  Modo: ' + 'Automático', True, c), (255, 438))
        elif(self.modo == 'M'):
            self.screen.blit(font.render('  Modo: ' + 'Manual', True, c), (255, 438))

    def dibujar_alerta(self):
        if(self.alerta == 1):
            width_height = (160, 40)
            pos_origen = (self.x_max//4 - width_height[0]//2 + 7, 203)
            pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(pos_origen, width_height))
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
        pygame.draw.rect(screen, (BLANCO), pygame.Rect(200 + delta3, 250 + delta3, 96,
                         int(146 - h1 * (146/50))))
        # Tanque 2:
        pygame.draw.rect(screen, c, pygame.Rect(340 + delta3, 250 + delta3, 96, 146))
        pygame.draw.rect(screen, (BLANCO), pygame.Rect(340 + delta3, 250 + delta3, 96,
                         int(146 - h2 * (146/50))))
        # Tanque 3:
        pygame.draw.rect(screen, c, pygame.Rect(200 + delta3, 30 + delta3, 96, 146))
        pygame.draw.rect(screen, (BLANCO), pygame.Rect(200 + delta3, 30 + delta3, 96,
                         int(146 - h3 * (146/50))))
        # Tanque 4:
        pygame.draw.rect(screen, c, pygame.Rect(340 + delta3, 30 + delta3, 96, 146))
        pygame.draw.rect(screen, (BLANCO), pygame.Rect(340 + delta3, 30 + delta3, 96,
                         int(146 - h4 * (146/50))))

    def actualizar(self, info_evento):
        self.alerta = info_evento[0]
        self.screen.fill(BLANCO)
        self.dibujar_todo()
        self.dibujar_h_t()
        self.dibujar_r_v()
        self.dibujar_modo()
        self.dibujar_alerta()
        self.dibujar_agua()
        if self.modo == "A":
            self.h_referencias()
        self.graficos.actualizar()
        self.constantes.dibujar_constantes()
        pygame.display.flip()

    def setear_variables(self, alturas, temp, razones, valvulas):
        self.alturas = alturas
        self.temp = temp
        self.razones = razones
        self.voltajes = valvulas
        self.graficos.actualizar_muestras(alturas, self.voltajes)


class GraficosInterfaz():
    def __init__(self, interfaz: Interfaz):
        self.screen = interfaz.screen
        self.res_x = 200
        self.res_y = 200
        # [Tanq1, Tanq2, Voltajes]
        self.origenes = [(710, 470), (1050, 470), (860, 220)]
        self.label = ["Altura Tanque 1", "Altura Tanque 2", "Voltajes de Válvulas"]
        self.len_muestras = 19
        self.muestras = [deque([0 for _ in range(self.len_muestras)]) for y in range(len(self.origenes)-1)]
        self.muestras.append(deque([0, 0] for _ in range(self.len_muestras)))
        self.font = pygame.font.Font('freesansbold.ttf', 12)
        self.font_graph = pygame.font.Font('freesansbold.ttf', 9)

    def dibujar_cartesianas(self):
        for origen in self.origenes:
            origen_arriba = (origen[0], origen[1]-self.res_y)
            origen_derecha = (origen[0]+self.res_x, origen[1])
            pygame.draw.line(self.screen, BLACK, origen, origen_arriba, 4)
            pygame.draw.line(self.screen, BLACK, origen, origen_derecha, 4)

    def dibujar_muestras(self):
        for y in range(len(self.origenes) - 1):
            origen = self.origenes[y]
            muestras = self.muestras[y]
            for x in range(len(muestras)):
                altura = muestras[x]
                pygame.draw.circle(self.screen, RED, (origen[0]+10*x+10,
                                   origen[1]-(18*altura//5 + 20)), 4)
        origen = self.origenes[-1]
        muestras = self.muestras[-1]
        for x in range(len(muestras)):
            (voltaje1, voltaje2) = tuple(muestras[x])
            pygame.draw.circle(self.screen, GREEN,
                               (origen[0]+10*x+10, origen[1]-(self.res_x-10)*voltaje1-10), 4)
            pygame.draw.circle(self.screen, BLUE,
                               (origen[0]+10*x+10, origen[1]-(self.res_x-10)*voltaje2-10), 3)

    def dibujarlabel(self):
        # Rallas verticales en eje x
        for origen in self.origenes:
            (pos_x, pos_y) = origen
            for x in range(20):
                pos_act_x = pos_x+10*x+10
                pygame.draw.line(self.screen, BLACK, (pos_act_x, pos_y), (pos_act_x, pos_y+5), 2)
        # Rallas horizontales en eje y
            for y in range(20):
                pos_act_y = pos_y-10*y-10
                pygame.draw.line(self.screen, BLACK, (pos_x, pos_act_y), (pos_x-5, pos_act_y), 2)
        # variable t en eje x
            self.screen.blit(self.font.render("t", True, BLACK), (pos_x+self.res_x, pos_y+10))
        # Labels
        for pos in range(len(self.origenes)):
            (pos_x, pos_y) = self.origenes[pos]
            self.screen.blit(self.font.render(self.label[pos], True, BLACK),
                             (pos_x+40, pos_y-self.res_y-20))
        for pos in range(len(self.origenes)-1):
            (pos_x, pos_y) = self.origenes[pos]
            # Numeros altura en eje y
            for y in range(20):
                pos_act_y = pos_y-10*y-14
                self.screen.blit(self.font_graph.render(str(int(50*y/19))+" cm", True, BLACK), (pos_x-34, pos_act_y))
        (pos_x, pos_y) = self.origenes[-1]
        # Numeros altura en eje y de voltaje
        for y in range(20):
            pos_act_y = pos_y-10*y-14
            self.screen.blit(self.font_graph.render(str(int(y/19))+"."+str(int((y*100/19)%100))+" V",
                             True, BLACK), (pos_x-35, pos_act_y))

    def actualizar_muestras(self, alturas, voltajes):
        for i in range(len(self.muestras)-1):
            lista = self.muestras[i]
            lista.rotate(-1)
            lista[-1] = alturas[i]
        lista = self.muestras[-1]
        lista.rotate(-1)
        lista[-1] = voltajes

    def actualizar(self):
        self.dibujar_cartesianas()
        self.dibujarlabel()
        self.dibujar_muestras()


class ConstantesInterfaz():
    def __init__(self, interfaz: Interfaz):
        self.screen = interfaz.screen
        self.font = pygame.font.Font('freesansbold.ttf', 12)
        self.font2 = pygame.font.Font(None, 32)

        self.texto = ''
        self.texto1 = ''
        self.texto2 = ''
        self.texto3 = ''
        self.texto4 = ''
        self.texto5 = ''
        self.texto6 = ''
        self.texto7 = ''
        self.texto8 = ''
        self.texto9 = ''
        self.texto10 = ''
        self.texto11 = ''
        self.texto12 = ''
        self.texto13 = ''
        self.texto14 = ''
        self.texto15 = ''
        self.texto16 = ''

        self.Kp1_input = ''
        self.Ki1_input = ''
        self.Kd1_input = ''
        self.Kp2_input = ''
        self.Ki2_input = ''
        self.Kd2_input = ''
        self.Kp3_input = ''
        self.Ki3_input = ''
        self.Kd3_input = ''
        self.Kp4_input = ''
        self.Ki4_input = ''
        self.Kd4_input = ''
        self.WuP1 = ''
        self.WuP2 = ''
        self.WuP3 = ''
        self.WuP4 = ''
        self.RAM = ''

        # create rectangle
        self.input_rect = pygame.Rect(50, 500, 100, 32)
        self.input_rect1 = pygame.Rect(200, 500, 100, 32)
        self.input_rect2 = pygame.Rect(350, 500, 100, 32)
        self.input_rect3 = pygame.Rect(50, 550, 100, 32)
        self.input_rect4 = pygame.Rect(200, 550, 100, 32)
        self.input_rect5 = pygame.Rect(350, 550, 100, 32)
        self.input_rect6 = pygame.Rect(500, 500, 100, 32)
        self.input_rect7 = pygame.Rect(500, 550, 100, 32)

        self.input_rect8 = pygame.Rect(650, 500, 100, 32)
        self.input_rect9 = pygame.Rect(800, 500, 100, 32)
        self.input_rect10 = pygame.Rect(950, 500, 100, 32)
        self.input_rect11 = pygame.Rect(650, 550, 100, 32)
        self.input_rect12 = pygame.Rect(800, 550, 100, 32)
        self.input_rect13 = pygame.Rect(950, 550, 100, 32)
        self.input_rect14 = pygame.Rect(1100, 500, 100, 32)
        self.input_rect15 = pygame.Rect(1100, 550, 100, 32)
        self.input_rect16 = pygame.Rect(500, 450, 100, 32)
        self.state_cte = 0

    def dibujar_constantes(self):
        self.screen.blit(self.font.render('Kp 1 =', True, (0, 0, 0)), (10, 510))
        self.screen.blit(self.font.render('Ki 1 =', True, (0, 0, 0)), (160, 510))
        self.screen.blit(self.font.render('Kd 1 =', True, (0, 0, 0)), (310, 510))
        self.screen.blit(self.font.render('Kp 2 =', True, (0, 0, 0)), (10, 555))
        self.screen.blit(self.font.render('Ki 2 =', True, (0, 0, 0)), (160, 555))
        self.screen.blit(self.font.render('Kd 2 =', True, (0, 0, 0)), (310, 555))
        self.screen.blit(self.font.render('Kp 3 =', True, (0, 0, 0)), (610, 510))
        self.screen.blit(self.font.render('Ki 3 =', True, (0, 0, 0)), (760, 510))
        self.screen.blit(self.font.render('Kd 3 =', True, (0, 0, 0)), (910, 510))
        self.screen.blit(self.font.render('Kp 4 =', True, (0, 0, 0)), (610, 555))
        self.screen.blit(self.font.render('Ki 4 =', True, (0, 0, 0)), (760, 555))
        self.screen.blit(self.font.render('Kd 4 =', True, (0, 0, 0)), (910, 555))
        self.screen.blit(self.font.render('Wp 1 =', True, (0, 0, 0)), (460, 510))
        self.screen.blit(self.font.render('Wp 2 =', True, (0, 0, 0)), (460, 555))
        self.screen.blit(self.font.render('Wp 3 =', True, (0, 0, 0)), (1060, 510))
        self.screen.blit(self.font.render('Wp 4 =', True, (0, 0, 0)), (1060, 555))
        self.screen.blit(self.font.render('RAM =', True, (0, 0, 0)), (460, 460))

        color = pygame.Color('lightskyblue3')

        # dibuja un rectángulo y se pasa un argumento que debería estar en pantalla
        pygame.draw.rect(self.screen, color, self.input_rect)
        pygame.draw.rect(self.screen, color, self.input_rect1)
        pygame.draw.rect(self.screen, color, self.input_rect2)
        pygame.draw.rect(self.screen, color, self.input_rect3)
        pygame.draw.rect(self.screen, color, self.input_rect4)
        pygame.draw.rect(self.screen, color, self.input_rect5)
        pygame.draw.rect(self.screen, color, self.input_rect6)
        pygame.draw.rect(self.screen, color, self.input_rect7)
        pygame.draw.rect(self.screen, color, self.input_rect8)
        pygame.draw.rect(self.screen, color, self.input_rect9)
        pygame.draw.rect(self.screen, color, self.input_rect10)
        pygame.draw.rect(self.screen, color, self.input_rect11)
        pygame.draw.rect(self.screen, color, self.input_rect12)
        pygame.draw.rect(self.screen, color, self.input_rect13)
        pygame.draw.rect(self.screen, color, self.input_rect14)
        pygame.draw.rect(self.screen, color, self.input_rect15)
        pygame.draw.rect(self.screen, color, self.input_rect16)

        if (self.state_cte == 1):
            # render en la posición indicada en los argumentos
            self.screen.blit(self.font2.render(self.texto, True, (BLANCO)),
                             (self.input_rect.x+5, self.input_rect.y+5))
            # establecer el ancho del campo de texto para que el texto no se pueda obtener fuera de
            # la entrada de texto del usuario
            self.input_rect.w = max(50, self.font2.render(self.texto, True,
                                    (BLANCO)).get_width()+10)
        if(self.state_cte == 2):
            self.screen.blit(self.font2.render(self.texto1, True, BLANCO), (self.input_rect1.x+5, self.input_rect1.y+5))
            self.input_rect1.w = max(50, self.font2.render(self.texto1, True, BLANCO).get_width()+10)
        if(self.state_cte == 3):
            self.screen.blit(self.font2.render(self.texto2, True, BLANCO), (self.input_rect2.x+5, self.input_rect2.y+5))
            self.input_rect2.w = max(50, self.font2.render(self.texto2, True, BLANCO).get_width()+10)
        if(self.state_cte == 4):
            self.screen.blit(self.font2.render(self.texto3, True, BLANCO), (self.input_rect3.x+5, self.input_rect3.y+5))
            self.input_rect3.w = max(50, self.font2.render(self.texto3, True, BLANCO).get_width()+10)
        if(self.state_cte == 5):
            self.screen.blit(self.font2.render(self.texto4, True, BLANCO), (self.input_rect4.x+5, self.input_rect4.y+5))
            self.input_rect4.w = max(50, self.font2.render(self.texto4, True, BLANCO).get_width()+10)
        if(self.state_cte == 6):
            self.screen.blit(self.font2.render(self.texto5, True, BLANCO), (self.input_rect5.x+5, self.input_rect5.y+5))
            self.input_rect5.w = max(50, self.font2.render(self.texto5, True, BLANCO).get_width()+10)
        if(self.state_cte == 7):
            self.screen.blit(self.font2.render(self.texto6, True, BLANCO), (self.input_rect6.x+5, self.input_rect6.y+5))
            self.input_rect6.w = max(50, self.font2.render(self.texto6, True, BLANCO).get_width()+10)
        if(self.state_cte == 8):
            self.screen.blit(self.font2.render(self.texto7, True, BLANCO), (self.input_rect7.x+5, self.input_rect7.y+5))
            self.input_rect7.w = max(50, self.font2.render(self.texto7, True, BLANCO).get_width()+10)
        if(self.state_cte == 9):
            self.screen.blit(self.font2.render(self.texto8, True, BLANCO), (self.input_rect8.x+5, self.input_rect8.y+5))
            self.input_rect8.w = max(50, self.font2.render(self.texto8, True, BLANCO).get_width()+10)
        if(self.state_cte == 10):
            self.screen.blit(self.font2.render(self.texto9, True, BLANCO), (self.input_rect9.x+5, self.input_rect9.y+5))
            self.input_rect9.w = max(50, self.font2.render(self.texto9, True, BLANCO).get_width()+10)
        if(self.state_cte == 11):
            self.screen.blit(self.font2.render(self.texto10, True, BLANCO), (self.input_rect10.x+5, self.input_rect10.y+5))
            self.input_rect10.w = max(50, self.font2.render(self.texto10, True, BLANCO).get_width()+10)
        if(self.state_cte == 12):
            self.screen.blit(self.font2.render(self.texto11, True, BLANCO), (self.input_rect11.x+5, self.input_rect11.y+5))
            self.input_rect11.w = max(50, self.font2.render(self.texto11, True, BLANCO).get_width()+10)
        if(self.state_cte == 13):
            self.screen.blit(self.font2.render(self.texto12, True, BLANCO), (self.input_rect12.x+5, self.input_rect12.y+5))
            self.input_rect12.w = max(50, self.font2.render(self.texto12, True, BLANCO).get_width()+10)
        if(self.state_cte == 14):
            self.screen.blit(self.font2.render(self.texto13, True, BLANCO), (self.input_rect13.x+5, self.input_rect13.y+5))
            self.input_rect13.w = max(50, self.font2.render(self.texto13, True, BLANCO).get_width()+10)
        if(self.state_cte == 15):
            self.screen.blit(self.font2.render(self.texto14, True, BLANCO), (self.input_rect14.x+5, self.input_rect14.y+5))
            self.input_rect14.w = max(50, self.font2.render(self.texto14, True, BLANCO).get_width()+10)
        if(self.state_cte == 16):
            self.screen.blit(self.font2.render(self.texto15, True, BLANCO), (self.input_rect15.x+5, self.input_rect15.y+5))
            self.input_rect15.w = max(50, self.font2.render(self.texto15, True, BLANCO).get_width()+10)
        if(self.state_cte == 17):
            self.screen.blit(self.font2.render(self.texto16, True, BLANCO), (self.input_rect16.x+5, self.input_rect16.y+5))
            self.input_rect16.w = max(50, self.font2.render(self.texto16, True, BLANCO).get_width()+10)


if __name__ == '__main__':
    pass
