from interfaz import Interfaz
from control import Control
import pygame
import sys


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


def eventos(interfaz: Interfaz, control: Control):
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
            if event.key == pygame.K_m:             # TECLA G: guardar datos
                control.state1 = "G"
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if (interfaz.constantes.state_cte == 1 and interfaz.constantes.texto.isnumeric()):
                    control.pid[0][0] = int(interfaz.constantes.texto)
                    print("Cambiando Kp_1 a", interfaz.constantes.texto)
                    interfaz.constantes.texto = ''
                elif (interfaz.constantes.state_cte == 2 and
                        interfaz.constantes.texto1.isnumeric()):
                    control.pid[0][1] = int(interfaz.constantes.texto1)
                    print("Cambiando Ki_1 a", interfaz.constantes.texto1)
                    interfaz.constantes.texto1 = ''
                elif (interfaz.constantes.state_cte == 3 and
                        interfaz.constantes.texto2.isnumeric()):
                    control.pid[0][2] = int(interfaz.constantes.texto2)
                    print("Cambiando Kd_1 a", interfaz.constantes.texto2)
                    interfaz.constantes.texto2 = ''

                elif (interfaz.constantes.state_cte == 4 and
                        interfaz.constantes.texto3.isnumeric()):
                    control.pid[1][0] = int(interfaz.constantes.texto3)
                    print("Cambiando Kp_2 a", interfaz.constantes.texto3)
                    interfaz.constantes.texto3 = ''
                elif (interfaz.constantes.state_cte == 5 and
                        interfaz.constantes.texto4.isnumeric()):
                    control.pid[1][1] = int(interfaz.constantes.texto4)
                    print("Cambiando Ki_2 a", interfaz.constantes.texto4)
                    interfaz.constantes.texto4 = ''
                elif (interfaz.constantes.state_cte == 6 and
                        interfaz.constantes.texto5.isnumeric()):
                    control.pid[1][2] = int(interfaz.constantes.texto5)
                    print("Cambiando Kd_2 a", interfaz.constantes.texto5)
                    interfaz.constantes.texto5 = ''

                elif (interfaz.constantes.state_cte == 7):
                    WuP1 = interfaz.constantes.texto6
                    interfaz.constantes.texto6 = ''
                elif (interfaz.constantes.state_cte == 8):
                    WuP2 = interfaz.constantes.texto7
                    interfaz.constantes.texto7 = ''

                elif (interfaz.constantes.state_cte == 9 and
                        interfaz.constantes.texto8.isnumeric()):
                    control.pid[2][0] = int(interfaz.constantes.texto8)
                    print("Cambiando Kp_3 a", interfaz.constantes.texto8)
                    interfaz.constantes.texto8 = ''
                elif (interfaz.constantes.state_cte == 10 and
                        interfaz.constantes.texto9.isnumeric()):
                    control.pid[2][1] = int(interfaz.constantes.texto9)
                    print("Cambiando Ki_3 a", interfaz.constantes.texto9)
                    interfaz.constantes.texto9 = ''
                elif (interfaz.constantes.state_cte == 11 and
                        interfaz.constantes.texto10.isnumeric()):
                    control.pid[2][2] = int(interfaz.constantes.texto10)
                    print("Cambiando Kd_3 a", interfaz.constantes.texto10)
                    interfaz.constantes.texto10 = ''

                elif (interfaz.constantes.state_cte == 12 and
                        interfaz.constantes.texto11.isnumeric()):
                    control.pid[3][0] = int(interfaz.constantes.texto11)
                    print("Cambiando Kp_4 a", interfaz.constantes.texto11)
                    interfaz.constantes.texto11 = ''
                elif (interfaz.constantes.state_cte == 13 and
                        interfaz.constantes.texto12.isnumeric()):
                    control.pid[3][1] = int(interfaz.constantes.texto12)
                    print("Cambiando Ki_4 a", interfaz.constantes.texto12)
                    interfaz.constantes.texto12 = ''
                elif (interfaz.constantes.state_cte == 14 and
                        interfaz.constantes.texto13.isnumeric()):
                    control.pid[3][2] = int(interfaz.constantes.texto13)
                    print("Cambiando Kd_4 a", interfaz.constantes.texto13)
                    interfaz.constantes.texto13 = ''

                elif (interfaz.constantes.state_cte == 15):
                    WuP3 = texto14
                    texto14 = ''
                elif (interfaz.constantes.state_cte == 16):
                    WuP4 = texto15
                    texto15 = ''

                elif (interfaz.constantes.state_cte == 17):
                    RAM = texto16
                    texto16 = ''

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


def funcion_handler(node, val):
    key = node.get_parent().get_display_name().Text
    print('key: {} | val: {}'.format(key, val))
