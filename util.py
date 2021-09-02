from interfaz import Interfaz
import pygame


def obtener(cliente, interfaz: Interfaz):
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


def Eventos(interfaz: Interfaz):
    LEFT = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:    # http://www.pygame.org/docs/ref/key.html
            if event.key == pygame.K_s:             # STOP
                interfaz.modo = "STOP"
            if event.key == pygame.K_LEFT:         # FLECHA IZQUIERDA: bajamos voltaje 2
                state1 = "BV2"
            if event.key == pygame.K_RIGHT:        # FLECHA DERECHA: subir voltaje 2
                state1 = "SV2"
            if event.key == pygame.K_UP:           # FLECHA ARRIBA: subir voltaje 1
                state1 = "SV1"
            if event.key == pygame.K_DOWN:          # FLECHA ABAJO: bajamos voltaje 1
                state1 = "BV1"
            if event.key == pygame.K_m:             # TECLA M: MANUAL
                interfaz.modo = "M"
            if event.key == pygame.K_a:             # TECLA A: AUTOMÁTICO
                interfaz.modo = "A"
            if event.key == pygame.K_m:             # TECLA G: guardar datos
                state1 = "G"
            if event.key == pygame.K_i:             # TECLA i: subir razon de flujo 1
                state1 = "SF1"
            if event.key == pygame.K_k:             # TECLA k: bajar razon de flujo 1
                state1 = "BF1"
            if event.key == pygame.K_l:             # TECLA l: subir razon de flujo 2
                state1 = "SF2"
            if event.key == pygame.K_j:             # TECLA j: bajar razon de flujo 2
                state1 = "BF2"
        if event.type == pygame.MOUSEBUTTONDOWN:    # MOUSE BTN IZQ CLICK
            if event.button == LEFT:
                state1 = "R"
                mouse_pos = pygame.mouse.get_pos()

    return True
