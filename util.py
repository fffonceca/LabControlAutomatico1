from interfaz import Interfaz
from control import Control
from collections import namedtuple, deque
import pygame
import sys


Estructura = namedtuple('Estructura_de_datos_G', ['Alturas', 'Referencias',
                        'Voltajes', 'PID', 'Razones'])


class BufferCircular():
    def __init__(self, RAM):
        self.inicializar(RAM)
        self.path_file = 'datos.txt'
        with open(self.path_file, mode='w', encoding='utf-8') as file:
            file.write("Alturas,Referencias,Voltajes,pid,Razones\n")

    def insertar_dato(self, interfaz, control):
        self.datos.rotate(-1)
        self.datos[-1] = Estructura(interfaz.alturas, interfaz.h_ref, interfaz.voltajes,
                                    control.pid, interfaz.razones)

    def inicializar(self, RAM):
        self.RAM = RAM
        self.datos = deque([0 for _ in range(self.RAM)])

    def cargar_datos(self):
        with open(self.path_file, mode='a', encoding='utf-8') as file:
            sum = 0
            for dato in self.datos:
                if dato != 0:
                    string_to_write = ""
                    string_to_write += " ".join([str(a) for a in dato.Alturas])
                    string_to_write += "," + " ".join([str(a) for a in dato.Referencias])
                    string_to_write += "," + " ".join([str(a) for a in dato.Voltajes])
                    x = list()
                    for i in dato.PID:
                        for y in i:
                            x.append(str(y))
                    string_to_write += "," + " ".join(x)
                    string_to_write += "," + " ".join([str(a) for a in dato.Razones]) + "\n"
                    file.write(string_to_write)
                    sum += 1
            print(f"Se escribieron {sum} datos")


def obtener(cliente, interfaz: Interfaz, control: Control):
    vm1 = cliente.valvulas['valvula1'].get_value()
    vm2 = cliente.valvulas['valvula2'].get_value()
    voltajes = [vm1, vm2]

    vr1 = cliente.razones['razon1'].get_value()
    vr2 = cliente.razones['razon2'].get_value()
    razones = [vr1, vr2]

    vc1 = cliente.alturas['H1'].get_value()
    vc2 = cliente.alturas['H2'].get_value()
    vc3 = cliente.alturas['H3'].get_value()
    vc4 = cliente.alturas['H4'].get_value()
    alturas = [vc1, vc2, vc3, vc4]

    temp1 = cliente.temperaturas['T1'].get_value()
    temp2 = cliente.temperaturas['T2'].get_value()
    temp3 = cliente.temperaturas['T3'].get_value()
    temp4 = cliente.temperaturas['T4'].get_value()
    temp = [temp1, temp2, temp3, temp4]

    interfaz.setear_variables(alturas, temp, razones, voltajes)
    control.setear_variables(alturas, [vm1, vm2, vr1, vr2])


def eventos(interfaz: Interfaz, control: Control, buffer: BufferCircular):
    LEFT = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    # http://www.pygame.org/docs/ref/key.html
            if event.key == pygame.K_s:             # STOP
                interfaz.modo = "STOP"
            if event.key == pygame.K_LEFT:         # FLECHA IZQUIERDA: bajamos voltaje 2
                control.state1 = "BV2"
            if event.key == pygame.K_RIGHT:        # FLECHA DERECHA: subir voltaje 2
                control.state1 = "SV2"
            if event.key == pygame.K_UP:           # FLECHA ARRIBA: subir voltaje 1
                control.state1 = "SV1"
            if event.key == pygame.K_DOWN:          # FLECHA ABAJO: bajamos voltaje 1
                control.state1 = "BV1"
            if event.key == pygame.K_m:             # TECLA M: MANUAL
                interfaz.modo = "M"
            if event.key == pygame.K_a:             # TECLA A: AUTOMÁTICO
                interfaz.modo = "A"
            if event.key == pygame.K_g:             # TECLA G: guardar datos
                buffer.cargar_datos()
            if event.key == pygame.K_i:             # TECLA i: subir razon de flujo 1
                control.state1 = "SF1"
            if event.key == pygame.K_k:             # TECLA k: bajar razon de flujo 1
                control.state1 = "BF1"
            if event.key == pygame.K_l:             # TECLA l: subir razon de flujo 2
                control.state1 = "SF2"
            if event.key == pygame.K_j:             # TECLA j: bajar razon de flujo 2
                control.state1 = "BF2"
        if event.type == pygame.MOUSEBUTTONDOWN:    # MOUSE BTN IZQ CLICK
            if event.button == LEFT:
                control.state1 = "R"
                control.mouse_pos = pygame.mouse.get_pos()
            if interfaz.constantes.input_rect.collidepoint(event.pos):
                interfaz.constantes.state_cte = 1
            elif interfaz.constantes.input_rect1.collidepoint(event.pos):
                interfaz.constantes.state_cte = 2
            elif interfaz.constantes.input_rect2.collidepoint(event.pos):
                interfaz.constantes.state_cte = 3
            elif interfaz.constantes.input_rect3.collidepoint(event.pos):
                interfaz.constantes.state_cte = 4
            elif interfaz.constantes.input_rect4.collidepoint(event.pos):
                interfaz.constantes.state_cte = 5
            elif interfaz.constantes.input_rect5.collidepoint(event.pos):
                interfaz.constantes.state_cte = 6
            elif interfaz.constantes.input_rect6.collidepoint(event.pos):
                interfaz.constantes.state_cte = 7
            elif interfaz.constantes.input_rect7.collidepoint(event.pos):
                interfaz.constantes.state_cte = 8
            elif interfaz.constantes.input_rect8.collidepoint(event.pos):
                interfaz.constantes.state_cte = 9
            elif interfaz.constantes.input_rect9.collidepoint(event.pos):
                interfaz.constantes.state_cte = 10
            elif interfaz.constantes.input_rect10.collidepoint(event.pos):
                interfaz.constantes.state_cte = 11
            elif interfaz.constantes.input_rect11.collidepoint(event.pos):
                interfaz.constantes.state_cte = 12
            elif interfaz.constantes.input_rect12.collidepoint(event.pos):
                interfaz.constantes.state_cte = 13
            elif interfaz.constantes.input_rect13.collidepoint(event.pos):
                interfaz.constantes.state_cte = 14
            elif interfaz.constantes.input_rect14.collidepoint(event.pos):
                interfaz.constantes.state_cte = 15
            elif interfaz.constantes.input_rect15.collidepoint(event.pos):
                interfaz.constantes.state_cte = 16
            elif interfaz.constantes.input_rect16.collidepoint(event.pos):
                interfaz.constantes.state_cte = 17
            else:
                interfaz.constantes.state_cte = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if (interfaz.constantes.state_cte == 1):
                    control.pid[0][0] = float(interfaz.constantes.texto)
                    print("Cambiando Kp_1 a", interfaz.constantes.texto)
                    interfaz.constantes.texto = ''
                elif (interfaz.constantes.state_cte == 2):
                    control.pid[0][1] = float(interfaz.constantes.texto1)
                    print("Cambiando Ki_1 a", interfaz.constantes.texto1)
                    interfaz.constantes.texto1 = ''
                elif (interfaz.constantes.state_cte == 3):
                    control.pid[0][2] = float(interfaz.constantes.texto2)
                    print("Cambiando Kd_1 a", interfaz.constantes.texto2)
                    interfaz.constantes.texto2 = ''

                elif (interfaz.constantes.state_cte == 4):
                    control.pid[1][0] = float(interfaz.constantes.texto3)
                    print("Cambiando Kp_2 a", interfaz.constantes.texto3)
                    interfaz.constantes.texto3 = ''
                elif (interfaz.constantes.state_cte == 5):
                    control.pid[1][1] = float(interfaz.constantes.texto4)
                    print("Cambiando Ki_2 a", interfaz.constantes.texto4)
                    interfaz.constantes.texto4 = ''
                elif (interfaz.constantes.state_cte == 6):
                    control.pid[1][2] = float(interfaz.constantes.texto5)
                    print("Cambiando Kd_2 a", interfaz.constantes.texto5)
                    interfaz.constantes.texto5 = ''

                elif (interfaz.constantes.state_cte == 7):
                    control.windup[0] = float(interfaz.constantes.texto6)
                    print("Cambiando WuP1 a", interfaz.constantes.texto6)
                    interfaz.constantes.texto6 = ''
                elif (interfaz.constantes.state_cte == 8):
                    control.windup[0] = float(interfaz.constantes.texto7)
                    print("Cambiando WuP2 a", interfaz.constantes.texto7)
                    interfaz.constantes.texto7 = ''

                elif (interfaz.constantes.state_cte == 9):
                    control.pid[2][0] = float(interfaz.constantes.texto8)
                    print("Cambiando Kp_3 a", interfaz.constantes.texto8)
                    interfaz.constantes.texto8 = ''
                elif (interfaz.constantes.state_cte == 10):
                    control.pid[2][1] = float(interfaz.constantes.texto9)
                    print("Cambiando Ki_3 a", interfaz.constantes.texto9)
                    interfaz.constantes.texto9 = ''
                elif (interfaz.constantes.state_cte == 11):
                    control.pid[2][2] = float(interfaz.constantes.texto10)
                    print("Cambiando Kd_3 a", interfaz.constantes.texto10)
                    interfaz.constantes.texto10 = ''

                elif (interfaz.constantes.state_cte == 12):
                    control.pid[3][0] = float(interfaz.constantes.texto11)
                    print("Cambiando Kp_4 a", interfaz.constantes.texto11)
                    interfaz.constantes.texto11 = ''
                elif (interfaz.constantes.state_cte == 13):
                    control.pid[3][1] = float(interfaz.constantes.texto12)
                    print("Cambiando Ki_4 a", interfaz.constantes.texto12)
                    interfaz.constantes.texto12 = ''
                elif (interfaz.constantes.state_cte == 14):
                    control.pid[3][2] = float(interfaz.constantes.texto13)
                    print("Cambiando Kd_4 a", interfaz.constantes.texto13)
                    interfaz.constantes.texto13 = ''

                elif (interfaz.constantes.state_cte == 15):
                    control.windup[2] = float(interfaz.constantes.texto14)
                    print("Cambiando WuP3 a", interfaz.constantes.texto14)
                    interfaz.constantes.texto14 = ''
                elif (interfaz.constantes.state_cte == 16):
                    control.windup[3] = float(interfaz.constantes.texto15)
                    print("Cambiando WuP4 a", interfaz.constantes.texto15)
                    interfaz.constantes.texto15 = ''

                elif (interfaz.constantes.state_cte == 17 and
                      interfaz.constantes.texto16.isnumeric()):
                    RAM = int(interfaz.constantes.texto16)
                    buffer.inicializar(RAM)
                    print("RAM ahora ocupa:", RAM)
                    interfaz.constantes.texto16 = ''

            # Verificar retroceso
            elif event.key == pygame.K_BACKSPACE:
                if (interfaz.constantes.state_cte == 1):
                    # obtenga la entrada de texto de 0 a -1, es decir, final.
                    interfaz.constantes.texto = interfaz.constantes.texto[:-1]
                elif (interfaz.constantes.state_cte == 2):
                    interfaz.constantes.texto1 = interfaz.constantes.texto1[:-1]
                elif (interfaz.constantes.state_cte == 3):
                    interfaz.constantes.texto2 = interfaz.constantes.texto2[:-1]
                elif (interfaz.constantes.state_cte == 4):
                    interfaz.constantes.texto3 = interfaz.constantes.texto3[:-1]
                elif (interfaz.constantes.state_cte == 5):
                    interfaz.constantes.texto4 = interfaz.constantes.texto4[:-1]
                elif (interfaz.constantes.state_cte == 6):
                    interfaz.constantes.texto5 = interfaz.constantes.texto5[:-1]
                elif (interfaz.constantes.state_cte == 7):
                    interfaz.constantes.texto6 = interfaz.constantes.texto6[:-1]
                elif (interfaz.constantes.state_cte == 8):
                    interfaz.constantes.texto7 = interfaz.constantes.texto7[:-1]
                elif (interfaz.constantes.state_cte == 9):
                    interfaz.constantes.texto8 = interfaz.constantes.texto8[:-1]
                elif (interfaz.constantes.state_cte == 10):
                    interfaz.constantes.texto9 = interfaz.constantes.texto9[:-1]
                elif (interfaz.constantes.state_cte == 11):
                    interfaz.constantes.texto10 = interfaz.constantes.texto10[:-1]
                elif (interfaz.constantes.state_cte == 12):
                    interfaz.constantes.texto11 = interfaz.constantes.texto11[:-1]
                elif (interfaz.constantes.state_cte == 13):
                    interfaz.constantes.texto12 = interfaz.constantes.texto12[:-1]
                elif (interfaz.constantes.state_cte == 14):
                    interfaz.constantes.texto13 = interfaz.constantes.texto13[:-1]
                elif (interfaz.constantes.state_cte == 15):
                    interfaz.constantes.texto14 = interfaz.constantes.texto14[:-1]
                elif (interfaz.constantes.state_cte == 16):
                    interfaz.constantes.texto15 = interfaz.constantes.texto15[:-1]
                elif (interfaz.constantes.state_cte == 17):
                    interfaz.constantes.texto16 = interfaz.constantes.texto16[:-1]

            # El estándar Unicode se usa para formación de cadenas
            else:
                if (interfaz.constantes.state_cte == 1):
                    interfaz.constantes.texto += event.unicode
                elif (interfaz.constantes.state_cte == 2):
                    interfaz.constantes.texto1 += event.unicode
                elif (interfaz.constantes.state_cte == 3):
                    interfaz.constantes.texto2 += event.unicode
                elif (interfaz.constantes.state_cte == 4):
                    interfaz.constantes.texto3 += event.unicode
                elif (interfaz.constantes.state_cte == 5):
                    interfaz.constantes.texto4 += event.unicode
                elif (interfaz.constantes.state_cte == 6):
                    interfaz.constantes.texto5 += event.unicode
                elif (interfaz.constantes.state_cte == 7):
                    interfaz.constantes.texto6 += event.unicode
                elif (interfaz.constantes.state_cte == 8):
                    interfaz.constantes.texto7 += event.unicode
                elif (interfaz.constantes.state_cte == 9):
                    interfaz.constantes.texto8 += event.unicode
                elif (interfaz.constantes.state_cte == 10):
                    interfaz.constantes.texto9 += event.unicode
                elif (interfaz.constantes.state_cte == 11):
                    interfaz.constantes.texto10 += event.unicode
                elif (interfaz.constantes.state_cte == 12):
                    interfaz.constantes.texto11 += event.unicode
                elif (interfaz.constantes.state_cte == 13):
                    interfaz.constantes.texto12 += event.unicode
                elif (interfaz.constantes.state_cte == 14):
                    interfaz.constantes.texto13 += event.unicode
                elif (interfaz.constantes.state_cte == 15):
                    interfaz.constantes.texto14 += event.unicode
                elif (interfaz.constantes.state_cte == 16):
                    interfaz.constantes.texto15 += event.unicode
                elif (interfaz.constantes.state_cte == 17):
                    interfaz.constantes.texto16 += event.unicode
    return True
