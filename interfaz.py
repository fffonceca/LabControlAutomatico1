from parametros import BLACK, CIAN, WHITE, RED, GREEN, BLUE
from collections import deque
import pygame


class Interfaz():
    def __init__(self, x_max=1280, y_max=665):
        # Screen
        self.x_max = x_max
        self.y_max = y_max
        self.alturas = [0, 0, 0, 0]
        self.temp = [20, 20, 20, 20]
        self.h_ref = [25, 25]
        self.razones = [0, 0]
        self.voltajes = [0, 0]
        self.modo = "A"
        self.alerta = False

    def init_interfaz(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.x_max, self.y_max])
        # Fonts
        self.font13 = pygame.font.Font('freesansbold.ttf', 13)
        self.font35 = pygame.font.Font('freesansbold.ttf', 35)
        self.font11 = pygame.font.Font('freesansbold.ttf', 11)
        # Rellenar con Blanco
        self.screen.fill(WHITE)
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
        pygame.draw.rect(self.screen, (201, 215, 154), pygame.Rect(50, 200, 170, 45))
        pygame.draw.rect(self.screen, (201, 215, 154), pygame.Rect(450, 200, 170, 45))

        # Cuadro verde oscuro
        pygame.draw.rect(self.screen, (150, 200, 150), pygame.Rect(710, 20, 200, 200))

        # Cuadro rojo claro
        pygame.draw.rect(self.screen, (251, 215, 194), pygame.Rect(250, 430, 140, 35))

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
        self.screen.blit(self.font13.render('Temperatura 1: '+str(round(t1, 2)) + '??C', True, c),
                         (55, 250 + 5 + 20 + 105))
        self.screen.blit(self.font13.render('Altura 2: ' + str(round(h2, 2)) + ' cm', True, c),
                         (340 + delta1 + 10 + 5, 250 + 5 + 105))
        self.screen.blit(self.font13.render('Temperatura 2: ' + str(round(t2, 2)) + '??C', True, c),
                         (340 + delta1 + 10 + 5, 250 + 5 + 20 + 105))
        self.screen.blit(self.font13.render('Altura 3: ' + str(round(h3, 2)) + ' cm', True, c),
                         (200 - 150 + 5, 30 + 5))
        self.screen.blit(self.font13.render('Temperatura 3: ' + str(round(t3, 2)) + '??C', True, c),
                         (200 - 150 + 5, 30 + 5 + 20))
        self.screen.blit(self.font13.render('Altura 4: ' + str(round(h4, 2)) + ' cm', True, c),
                         (340 + delta1 + 10 + 5, 30 + 5))
        self.screen.blit(self.font13.render('Temperatura 4: ' + str(round(t4, 2)) + '??C', True, c),
                         (340 + delta1 + 10 + 5, 30 + 5 + 20))

    def dibujar_r_v(self):
        (razon1, razon2) = self.razones
        (voltaje1, voltaje2) = self.voltajes
        font = self.font13
        c = BLACK
        self.screen.blit(font.render('Raz??n de Flujo 1: '+str(round(razon1, 2)), True, c),
                         (55, 205))
        self.screen.blit(font.render('Voltaje V??lvula 1: '+str(round(voltaje1, 2)) + ' V', True, c),
                         (55, 225))
        self.screen.blit(font.render('Raz??n de Flujo 2: '+str(round(razon2, 2)), True, c),
                         (455, 205))
        self.screen.blit(font.render('Voltaje V??lvula 2: '+str(round(voltaje2, 2)) + ' V', True, c),
                         (455, 225))

    def dibujar_modo(self):
        c = BLACK
        font = self.font13
        if(self.modo == 'A'):
            self.screen.blit(font.render('  Modo: ' + 'Autom??tico', True, c), (255, 438))
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
        pygame.draw.rect(screen, (WHITE), pygame.Rect(200 + delta3, 250 + delta3, 96,
                         int(146 - h1 * (146/50))))
        # Tanque 2:
        pygame.draw.rect(screen, c, pygame.Rect(340 + delta3, 250 + delta3, 96, 146))
        pygame.draw.rect(screen, (WHITE), pygame.Rect(340 + delta3, 250 + delta3, 96,
                         int(146 - h2 * (146/50))))
        # Tanque 3:
        pygame.draw.rect(screen, c, pygame.Rect(200 + delta3, 30 + delta3, 96, 146))
        pygame.draw.rect(screen, (WHITE), pygame.Rect(200 + delta3, 30 + delta3, 96,
                         int(146 - h3 * (146/50))))
        # Tanque 4:
        pygame.draw.rect(screen, c, pygame.Rect(340 + delta3, 30 + delta3, 96, 146))
        pygame.draw.rect(screen, (WHITE), pygame.Rect(340 + delta3, 30 + delta3, 96,
                         int(146 - h4 * (146/50))))

    def dibujar_parametros(self, control):
        pid = control.pid
        windup = control.windup
        self.screen.blit(self.font11.render("Par??metros de control PID: ", True, BLACK), (720, 35))
        self.screen.blit(self.font11.render("Kp 1: " + str(pid[0][0]), True, BLACK), (720, 60))
        self.screen.blit(self.font11.render("Ki 1: " + str(pid[0][1]), True, BLACK), (780, 60))
        self.screen.blit(self.font11.render("Kd 1: " + str(pid[0][2]), True, BLACK), (840, 60))
        self.screen.blit(self.font11.render("Kp 2: " + str(pid[1][0]), True, BLACK), (720, 80))
        self.screen.blit(self.font11.render("Ki 2: " + str(pid[1][1]), True, BLACK), (780, 80))
        self.screen.blit(self.font11.render("Kd 2: " + str(pid[1][2]), True, BLACK), (840, 80))
        self.screen.blit(self.font11.render("Kp 3: " + str(pid[2][0]), True, BLACK), (720, 100))
        self.screen.blit(self.font11.render("Ki 3: " + str(pid[2][1]), True, BLACK), (780, 100))
        self.screen.blit(self.font11.render("Kd 3: " + str(pid[2][2]), True, BLACK), (840, 100))
        self.screen.blit(self.font11.render("Kp 4: " + str(pid[3][0]), True, BLACK), (720, 120))
        self.screen.blit(self.font11.render("Ki 4: " + str(pid[3][1]), True, BLACK), (780, 120))
        self.screen.blit(self.font11.render("Kd 4: " + str(pid[3][2]), True, BLACK), (840, 120))
        self.screen.blit(self.font11.render("Par??metros de WindUp: ", True, BLACK), (720, 145))
        self.screen.blit(self.font11.render("Wi 1: " + str(windup[0]), True, BLACK), (720, 170))
        self.screen.blit(self.font11.render("Ws 1: " + str(windup[1]), True, BLACK), (780, 170))
        self.screen.blit(self.font11.render("Wi 2: " + str(windup[2]), True, BLACK), (720, 190))
        self.screen.blit(self.font11.render("Ws 2: " + str(windup[3]), True, BLACK), (780, 190))

    def actualizar(self, info_evento, control):
        self.alerta = info_evento[0]
        self.screen.fill(WHITE)
        self.dibujar_todo()
        self.dibujar_h_t()
        self.dibujar_r_v()
        self.dibujar_modo()
        self.dibujar_alerta()
        self.dibujar_agua()
        self.dibujar_parametros(control)
        if self.modo == "A":
            self.h_referencias()
        self.graficos.actualizar(self)
        self.constantes.dibujar_constantes()
        pygame.display.flip()

    def setear_variables(self, alturas, temp, razones, valvulas):
        self.alturas = alturas
        self.temp = temp
        self.razones = razones
        self.voltajes = valvulas


class GraficosInterfaz():
    def __init__(self, interfaz: Interfaz):
        self.screen = interfaz.screen
        self.res_x = 200
        self.res_y = 200
        self.origenes = [(710, 470), (980, 470), (980, 220)]
        self.len_muestras = 19
        len_origenes = len(self.origenes)
        len_mues = self.len_muestras
        self.label = ["  Altura Tanque 1", "  Altura Tanque 2", " Voltajes de V??lvulas"]
        self.muestras = [deque([0 for _ in range(len_mues)]) for y in range(len_origenes-1)]
        self.muestras.append(deque([0, 0] for _ in range(self.len_muestras)))
        self.font = pygame.font.Font('freesansbold.ttf', 12)
        self.font_graph = pygame.font.Font('freesansbold.ttf', 9)

    def dibujar_cartesianas(self):
        for origen in self.origenes:
            origen_arriba = (origen[0], origen[1]-self.res_y)
            origen_derecha = (origen[0]+self.res_x, origen[1])
            pygame.draw.line(self.screen, BLACK, origen, origen_arriba, 4)
            pygame.draw.line(self.screen, BLACK, origen, origen_derecha, 4)
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

    def dibujar_muestras(self):
        for y in range(len(self.origenes) - 1):
            origen = self.origenes[y]
            muestras = self.muestras[y]
            for x in range(len(muestras)):
                altura = muestras[x]
                pygame.draw.circle(self.screen, RED, (origen[0]+10*x+10,
                                   origen[1]-(18*altura/5 + 10)), 4)
        origen = self.origenes[-1]
        muestras = self.muestras[-1]
        for x in range(len(muestras)):
            (voltaje1, voltaje2) = tuple(muestras[x])
            pygame.draw.circle(self.screen, GREEN,
                               (origen[0]+10*x+10, origen[1]-(self.res_x-10)*voltaje1-10), 4)
            pygame.draw.circle(self.screen, BLUE,
                               (origen[0]+10*x+10, origen[1]-(self.res_x-10)*voltaje2-10), 3)

    def dibujar_label(self):
        # Labels
        for pos in range(len(self.origenes)):
            (pos_x, pos_y) = self.origenes[pos]
            self.screen.blit(self.font.render(self.label[pos], True, BLACK),
                             (pos_x+40, pos_y-self.res_y-20))
        # Numeros altura en eje y
        for pos in range(len(self.origenes)-1):
            (pos_x, pos_y) = self.origenes[pos]
            for y in range(20):
                pos_act_y = pos_y-10*y-14
                string_to_print = str(int(50*y/19))+" cm"
                self.screen.blit(self.font_graph.render(string_to_print, True, BLACK),
                                 (pos_x-34, pos_act_y))
        # Numeros altura en eje y de voltaje
        (pos_x, pos_y) = self.origenes[-1]
        for y in range(20):
            pos_act_y = pos_y-10*y-14
            num = str(y/19)
            string_to_print = num[0] + "." + num[2:4] + " V"
            self.screen.blit(self.font_graph.render(string_to_print, True, BLACK),
                             (pos_x-35, pos_act_y))
        # Dibujar leyenda voltaje 1 y voltaje 2
        pos_circulo_1 = (pos_x + self.res_x + 20, pos_y - 3*self.res_y//4)
        pos_leyenda_1 = (pos_circulo_1[0] + 10, pos_circulo_1[1] - 7)
        pygame.draw.circle(self.screen, GREEN, pos_circulo_1, 5)
        self.screen.blit(self.font.render("Voltaje 1", True, BLACK), pos_leyenda_1)

        pos_circulo_2 = (pos_x + self.res_x + 20, pos_y - 3*self.res_y//4 + 30)
        pos_leyenda_2 = (pos_circulo_2[0] + 10, pos_circulo_2[1] - 7)
        pygame.draw.circle(self.screen, BLUE, pos_circulo_2, 5)
        self.screen.blit(self.font.render("Voltaje 2", True, BLACK), pos_leyenda_2)

    def dibujar_refs(self, interfaz):
        refs = interfaz.h_ref
        if interfaz.modo == "A":
            for pos in range(len(self.origenes)-1):
                origen = self.origenes[pos]
                altura = origen[1]-(18*refs[pos]//5 + 20)
                izquierda = (origen[0], altura)
                derecha = (origen[0] + self.res_x, altura)
                pygame.draw.line(self.screen, (163, 73, 164), izquierda, derecha, 2)

    def actualizar_muestras(self, alturas, voltajes):
        for i in range(len(self.muestras)-1):
            lista = self.muestras[i]
            lista.rotate(-1)
            lista[-1] = alturas[i]
        lista = self.muestras[-1]  # lista de voltajes = [[1, 0], [1, 0], [0, 0]..., [0, 0]]
        lista.rotate(-1)  # lista [[1, 0], [0, 0],...., [0, 0], [1,0]]
        lista[-1][0] = voltajes[0]  # voltajes = [1, 0]
        lista[-1][1] = voltajes[1]

    def actualizar(self, interfaz):
        self.dibujar_cartesianas()
        self.dibujar_label()
        self.dibujar_refs(interfaz)
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
        self.input_rect = pygame.Rect(60, 550, 100, 32)
        self.input_rect1 = pygame.Rect(210, 550, 100, 32)
        self.input_rect2 = pygame.Rect(360, 550, 100, 32)
        self.input_rect3 = pygame.Rect(60, 600, 100, 32)
        self.input_rect4 = pygame.Rect(210, 600, 100, 32)
        self.input_rect5 = pygame.Rect(360, 600, 100, 32)
        self.input_rect6 = pygame.Rect(510, 550, 100, 32)
        self.input_rect7 = pygame.Rect(510, 600, 100, 32)
        self.input_rect8 = pygame.Rect(660, 550, 100, 32)
        self.input_rect9 = pygame.Rect(810, 550, 100, 32)
        self.input_rect10 = pygame.Rect(960, 550, 100, 32)
        self.input_rect11 = pygame.Rect(660, 600, 100, 32)
        self.input_rect12 = pygame.Rect(810, 600, 100, 32)
        self.input_rect13 = pygame.Rect(960, 600, 100, 32)
        self.input_rect14 = pygame.Rect(1110, 550, 100, 32)
        self.input_rect15 = pygame.Rect(1110, 600, 100, 32)
        self.input_rect16 = pygame.Rect(70, 500, 100, 32)
        self.state_cte = 0

    def dibujar_constantes(self):
        self.screen.blit(self.font.render('Kp 1 =', True, (0, 0, 0)), (20, 560))
        self.screen.blit(self.font.render('Ki 1 =', True, (0, 0, 0)), (170, 560))
        self.screen.blit(self.font.render('Kd 1 =', True, (0, 0, 0)), (320, 560))
        self.screen.blit(self.font.render('Kp 2 =', True, (0, 0, 0)), (20, 605))
        self.screen.blit(self.font.render('Ki 2 =', True, (0, 0, 0)), (170, 605))
        self.screen.blit(self.font.render('Kd 2 =', True, (0, 0, 0)), (320, 605))
        self.screen.blit(self.font.render('Kp 3 =', True, (0, 0, 0)), (620, 560))
        self.screen.blit(self.font.render('Ki 3 =', True, (0, 0, 0)), (770, 560))
        self.screen.blit(self.font.render('Kd 3 =', True, (0, 0, 0)), (920, 560))
        self.screen.blit(self.font.render('Kp 4 =', True, (0, 0, 0)), (620, 605))
        self.screen.blit(self.font.render('Ki 4 =', True, (0, 0, 0)), (770, 605))
        self.screen.blit(self.font.render('Kd 4 =', True, (0, 0, 0)), (920, 605))
        self.screen.blit(self.font.render('Wi 1 =', True, (0, 0, 0)), (470, 560))
        self.screen.blit(self.font.render('Ws 1 =', True, (0, 0, 0)), (470, 605))
        self.screen.blit(self.font.render('Wi 2 =', True, (0, 0, 0)), (1070, 560))
        self.screen.blit(self.font.render('Ws 2 =', True, (0, 0, 0)), (1070, 605))
        self.screen.blit(self.font.render('DATA =', True, (0, 0, 0)), (20, 510))

        color = pygame.Color('lightskyblue3')

        # dibuja un rect??ngulo y se pasa un argumento que deber??a estar en pantalla
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
        pygame.draw.rect(self.screen, (244, 177, 187), self.input_rect16)

        if (self.state_cte == 1):
            # render en la posici??n indicada en los argumentos
            self.screen.blit(self.font2.render(self.texto, True, (WHITE)),
                             (self.input_rect.x+5, self.input_rect.y+5))
            # establecer el ancho del campo de texto para que el texto no se pueda obtener fuera de
            # la entrada de texto del usuario
            self.input_rect.w = max(50, self.font2.render(self.texto, True,
                                    (WHITE)).get_width()+10)
        if(self.state_cte == 2):
            self.screen.blit(self.font2.render(self.texto1, True, WHITE),
                             (self.input_rect1.x+5, self.input_rect1.y+5))
            self.input_rect1.w = max(50, self.font2.render(self.texto1, True, WHITE).get_width()+10)
        if(self.state_cte == 3):
            self.screen.blit(self.font2.render(self.texto2, True, WHITE),
                             (self.input_rect2.x+5, self.input_rect2.y+5))
            self.input_rect2.w = max(50, self.font2.render(self.texto2, True, WHITE).get_width()+10)
        if(self.state_cte == 4):
            self.screen.blit(self.font2.render(self.texto3, True, WHITE),
                             (self.input_rect3.x+5, self.input_rect3.y+5))
            self.input_rect3.w = max(50, self.font2.render(self.texto3, True, WHITE).get_width()+10)
        if(self.state_cte == 5):
            self.screen.blit(self.font2.render(self.texto4, True, WHITE),
                             (self.input_rect4.x+5, self.input_rect4.y+5))
            self.input_rect4.w = max(50, self.font2.render(self.texto4, True, WHITE).get_width()+10)
        if(self.state_cte == 6):
            self.screen.blit(self.font2.render(self.texto5, True, WHITE),
                             (self.input_rect5.x+5, self.input_rect5.y+5))
            self.input_rect5.w = max(50, self.font2.render(self.texto5, True, WHITE).get_width()+10)
        if(self.state_cte == 7):
            self.screen.blit(self.font2.render(self.texto6, True, WHITE),
                             (self.input_rect6.x+5, self.input_rect6.y+5))
            self.input_rect6.w = max(50, self.font2.render(self.texto6, True, WHITE).get_width()+10)
        if(self.state_cte == 8):
            self.screen.blit(self.font2.render(self.texto7, True, WHITE),
                             (self.input_rect7.x+5, self.input_rect7.y+5))
            self.input_rect7.w = max(50, self.font2.render(self.texto7, True, WHITE).get_width()+10)
        if(self.state_cte == 9):
            self.screen.blit(self.font2.render(self.texto8, True, WHITE),
                             (self.input_rect8.x+5, self.input_rect8.y+5))
            self.input_rect8.w = max(50, self.font2.render(self.texto8, True, WHITE).get_width()+10)
        if(self.state_cte == 10):
            self.screen.blit(self.font2.render(self.texto9, True, WHITE),
                             (self.input_rect9.x+5, self.input_rect9.y+5))
            self.input_rect9.w = max(50, self.font2.render(self.texto9, True, WHITE).get_width()+10)
        if(self.state_cte == 11):
            self.screen.blit(self.font2.render(self.texto10, True, WHITE),
                             (self.input_rect10.x+5, self.input_rect10.y+5))
            self.input_rect10.w = max(50, self.font2.render(self.texto10,
                                                            True, WHITE).get_width()+10)
        if(self.state_cte == 12):
            self.screen.blit(self.font2.render(self.texto11, True, WHITE),
                             (self.input_rect11.x+5, self.input_rect11.y+5))
            self.input_rect11.w = max(50, self.font2.render(self.texto11,
                                                            True, WHITE).get_width()+10)
        if(self.state_cte == 13):
            self.screen.blit(self.font2.render(self.texto12, True, WHITE),
                             (self.input_rect12.x+5, self.input_rect12.y+5))
            self.input_rect12.w = max(50, self.font2.render(self.texto12,
                                                            True, WHITE).get_width()+10)
        if(self.state_cte == 14):
            self.screen.blit(self.font2.render(self.texto13, True, WHITE),
                             (self.input_rect13.x+5, self.input_rect13.y+5))
            self.input_rect13.w = max(50, self.font2.render(self.texto13, True,
                                                            WHITE).get_width()+10)
        if(self.state_cte == 15):
            self.screen.blit(self.font2.render(self.texto14, True, WHITE),
                             (self.input_rect14.x+5, self.input_rect14.y+5))
            self.input_rect14.w = max(50, self.font2.render(self.texto14,
                                                            True, WHITE).get_width()+10)
        if(self.state_cte == 16):
            self.screen.blit(self.font2.render(self.texto15, True, WHITE),
                             (self.input_rect15.x+5, self.input_rect15.y+5))
            self.input_rect15.w = max(50, self.font2.render(self.texto15,
                                                            True, WHITE).get_width()+10)
        if(self.state_cte == 17):
            self.screen.blit(self.font2.render(self.texto16, True, WHITE),
                             (self.input_rect16.x+5, self.input_rect16.y+5))
            self.input_rect16.w = max(50, self.font2.render(self.texto16,
                                                            True, WHITE).get_width()+10)


if __name__ == '__main__':
    pass
