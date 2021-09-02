# LIBRERIAS:
from Libreria.cliente import Cliente
from pygame.locals import *
from util import obtener
import pygame
import threading

# VARIABLES GLOBALES:
XMAX = 640
YMAX = 600
mouse_pos = (0, 0)
state = "A"
state1 = "  "
vm = [0.4, 0.4, 0.35, 0.35]  # v1, v2, r1, r2
vc = [50, 50, 50, 50]  # h1, h2, h3, h4
temp = [0, 0, 0, 0]
h_ref = [25.00, 25.00]  # ht1, ht2
pid = [100, 1, 1, 100, 1, 1, 100, 1, 1, 100, 1, 1]  # Kp, Ki, Kd (1,2,3,4)
h_error = [0, 0, 0, 0, 0, 0]  # error v1, error v1 old, error v1 old2, error v2, error v2 old, error v2 old2
es_evento = False
programa_evento = 0


def funcion_handler(node, val):
    key = node.get_parent().get_display_name().Text
    print('key: {} | val: {}'.format(key, val))


class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    data_change and event methods are called directly from receiving thread.
    Do not do expensive, slow or network operation there. Create another
    thread if you need to do such a thing
    """
    def datachange_notification(self, node, val, data):
        thread_handler = threading.Thread(target=funcion_handler, args=(node, val))
        thread_handler.start()

    # Eventos!!
    def event_notification(self, event):
        global es_evento, programa_evento
        es_evento = True
        programa_evento = event


def Inicio():
    global XMAX, YMAX, screen
    pygame.init()       # Initialize PyGame and setup a PyGame display
    screen = pygame.display.set_mode((XMAX, YMAX))
    pygame.display.set_caption('Experiencia 1: Control de Procesos')
    # Works with essentially no delay, pygame.key.set_repeat(0,50),
    # Doesn't work because when the delay is set to zero,
    # key.set_repeat is returned to the default, disabled state.
    pygame.key.set_repeat(1, 50)


def Pantalla(c, delta1, delta2, font):
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (640, 0), 4)
    pygame.draw.line(screen, (0, 0, 0), (640, 0), (640, 480), 4)
    pygame.draw.line(screen, (0, 0, 0), (640, 480), (640, 0), 4)
    pygame.draw.line(screen, (0, 0, 0), (640, 0), (0, 0), 4)

    # Cuadros verdes claros
    pygame.draw.rect(screen, (201, 215, 154), pygame.Rect(50, 200, 150, 45))
    pygame.draw.rect(screen, (201, 215, 154), pygame.Rect(450, 200, 150, 45))

    # Cuadro rojo claro
    pygame.draw.rect(screen, (251, 215, 194), pygame.Rect(250, 425, 140, 45))

    # Cuadros morados claros
    pygame.draw.rect(screen, (201, 154, 215), pygame.Rect(200 - 150, 30, 140, 45))
    pygame.draw.rect(screen, (201, 154, 215), pygame.Rect(340 + delta1 + 10, 30, 140, 45))
    pygame.draw.rect(screen, (201, 154, 215), pygame.Rect(200 - 150, 250 + 105, 140, 45))
    pygame.draw.rect(screen, (201, 154, 215), pygame.Rect(340 + delta1 + 10, 250 + 105, 140, 45))

    screen.blit(font.render('Tank 1', True, c), (200 + 30, 250 + delta2 + 7))
    screen.blit(font.render('Tank 2', True, c), (340 + 30, 250 + delta2 + 7))
    screen.blit(font.render('Tank 3', True, c), (200 + 30, 30 + delta2 + 7))
    screen.blit(font.render('Tank 4', True, c), (340 + 30, 30 + delta2 + 7))

    lineas_estanque(200, 250, c, delta1, delta2)  # 1
    lineas_estanque(340, 250, c, delta1, delta2)  # 2
    lineas_estanque(200, 30, c, delta1, delta2)  # 3
    lineas_estanque(340, 30, c, delta1, delta2)  # 4


def h_referencias(h_ref, font):
    screen.blit(font.render('ref: ' + str(round(h_ref[0], 2)), True, (2, 25, 153)), (225, 310))
    screen.blit(font.render('ref: ' + str(round(h_ref[1], 2)), True, (2, 25, 153)), (365, 310))


def lineas_estanque(x, y, c, delta1, delta2):
    pygame.draw.line(screen, c, (x, y), (x + delta1, y), 4)
    pygame.draw.line(screen, c, (x, y), (x, y + delta2), 4)
    pygame.draw.line(screen, c, (x + delta1, y), (x + delta1, y + delta2), 4)
    pygame.draw.line(screen, c, (x, y + delta2), (x + delta1, y + delta2), 4)


def HyT(h1, h2, h3, h4, t1, t2, t3, t4, c, delta1, delta2, font):
    screen.blit(font.render('Altura 1: '+str(round(h1, 2)), True, c), (55, 360))
    screen.blit(font.render('Temperatura 1: '+str(round(t1, 2)), True, c),
                (55, 250 + 5 + 20 + 105))
    screen.blit(font.render('Altura 2: ' + str(round(h2, 2)), True, c),
                (340 + delta1 + 10 + 5, 250 + 5 + 105))
    screen.blit(font.render('Temperatura 2: ' + str(round(t2, 2)), True, c),
                (340 + delta1 + 10 + 5, 250 + 5 + 20 + 105))
    screen.blit(font.render('Altura 3: ' + str(round(h3, 2)), True, c),
                (200 - 150 + 5, 30 + 5))
    screen.blit(font.render('Temperatura 3: ' + str(round(t3, 2)), True, c),
                (200 - 150 + 5, 30 + 5 + 20))
    screen.blit(font.render('Altura 4: ' + str(round(h4, 2)), True, c),
                (340 + delta1 + 10 + 5, 30 + 5))
    screen.blit(font.render('Temperatura 4: ' + str(round(t4, 2)), True, c),
                (340 + delta1 + 10 + 5, 30 + 5 + 20))


def RyV(razon1, razon2, voltaje1, voltaje2, c, font):
    screen.blit(font.render('Razón de Flujo 1: '+str(round(razon1, 2)), True, c), (55, 205))
    screen.blit(font.render('Voltaje Válvula 1: '+str(round(voltaje1, 2)), True, c), (55, 225))
    screen.blit(font.render('Razón de Flujo 2: '+str(round(razon2, 2)), True, c), (455, 205))
    screen.blit(font.render('Voltaje Válvula 2: '+str(round(voltaje2, 2)), True, c), (455, 225))


def Alerta(alerta, font):
    if(alerta == 1):
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(0, 200, 640, 45))
        font = pygame.font.Font('freesansbold.ttf', 35)
        screen.blit(font.render('ALERTA', True, (255, 0, 0)), (260, 208))


def Modo(modo, c, font):
    if(modo == 'A'):
        screen.blit(font.render('Modo: ' + 'Automático', True, c), (255, 430))
    elif(modo == 'M'):
        screen.blit(font.render('Modo: ' + 'Manual', True, c), (255, 430))


def Agua(c, h1, h2, h3, h4, delta1, delta2):
    delta3 = 3
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


def Interfaz(modo, vc, temp, h_ref, pid, vm, alerta):
    black = (0, 0, 0)
    cian = (0, 255, 255)
    delta1 = 100
    delta2 = 150
    screen.fill((255, 255, 255))  # TIRA ERROR RARO
    font = pygame.font.Font('freesansbold.ttf', 13)
    Pantalla(black, delta1, delta2, font)
    HyT(vc[0], vc[1], vc[2], vc[3], temp[0], temp[1], temp[2], temp[3], black, delta1, delta2, font)
    RyV(vm[2], vm[3], vm[0], vm[1], black, font)
    Modo(modo, black, font)
    Alerta(alerta, font)
    Agua(cian, vc[0], vc[1], vc[2], vc[3], delta1, delta2)
    if modo == "A":
        h_referencias(h_ref, font)
    pygame.display.flip()


def Obtener():
    global vc, vm, temp  # vm: v1, v2, r1, r2 | vc: h1, h2, h3, h4
    vm[0] = cliente.valvulas['valvula1'].get_value()
    vm[1] = cliente.valvulas['valvula2'].get_value()
    vm[2] = cliente.razones['razon1'].get_value()
    vm[3] = cliente.razones['razon2'].get_value()
    vc[0] = cliente.alturas['H1'].get_value()
    vc[1] = cliente.alturas['H2'].get_value()
    vc[2] = cliente.alturas['H3'].get_value()
    vc[3] = cliente.alturas['H4'].get_value()
    temp[0] = cliente.temperaturas['T1'].get_value()
    temp[1] = cliente.temperaturas['T2'].get_value()
    temp[2] = cliente.temperaturas['T3'].get_value()
    temp[3] = cliente.temperaturas['T4'].get_value()
    Alarma()


def Alarma():
    # El objeto programa_evento es el evento mismo
    global es_evento, programa_evento
    if (es_evento):
        print(programa_evento.Message)
        print(programa_evento.Nivel)
        print(programa_evento.Mensaje)
        print(programa_evento.Severity)
        es_evento = False


def Eventos():
    global mouse_pos, state, state1
    LEFT = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:    # http://www.pygame.org/docs/ref/key.html
            if event.key == pygame.K_s:             # STOP
                state = "STOP"
            if event.key == pygame.K_LEFT:         # FLECHA IZQUIERDA: bajamos voltaje 2
                state1 = "BV2"
            if event.key == pygame.K_RIGHT:        # FLECHA DERECHA: subir voltaje 2
                state1 = "SV2"
            if event.key == pygame.K_UP:           # FLECHA ARRIBA: subir voltaje 1
                state1 = "SV1"
            if event.key == pygame.K_DOWN:          # FLECHA ABAJO: bajamos voltaje 1
                state1 = "BV1"
            if event.key == pygame.K_m:             # TECLA M: MANUAL
                state = "M"
            if event.key == pygame.K_a:             # TECLA A: AUTOMÁTICO
                state = "A"
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


def Control():
    global h_ref, state, state1, vm, vc, mouse_pos, pid, h_error
    sensi = 0.1
    Ts = 0.01
    if(state == "A"):
        # CAMBIO DE REFERENCIA
        if state1 == "R":
            if 202 < mouse_pos[0] < 300 and 252 < mouse_pos[1] < 400:
                h_ref[0] = (mouse_pos[1] - 399) * (- 50 / 146)
            if 342 < mouse_pos[0] < 440 and 252 < mouse_pos[1] < 400:
                h_ref[1] = (mouse_pos[1] - 399) * (- 50 / 146)
            state1 = " "

        #DEFINICIÓN DE ERRORES
        h_error[0] = h_ref[0] - vc[0]
        h_error[3] = h_ref[1] - vc[1]
        
        #CONTROL PID
        vm[0] += pid[0] * (h_error[0] - h_error[1]) + pid[1] * Ts * h_error[0] + pid[2] * (h_error[0] - h_error[1] + h_error[2]) / Ts
        vm[0] += pid[3] * (h_error[3] - h_error[4]) + pid[4] * Ts * h_error[3] + pid[5] * (h_error[3] - h_error[4] + h_error[5]) / Ts
        vm[1] += pid[6] * (h_error[0] - h_error[1]) + pid[7] * Ts * h_error[0] + pid[8] * (h_error[0] - h_error[1] + h_error[2]) / Ts
        vm[1] += pid[9] * (h_error[3] - h_error[4]) + pid[10] * Ts * h_error[3] + pid[11] * (h_error[3] - h_error[4] + h_error[5]) / Ts
        #ANTI WINDUP
        if vm[0] > 1:
            vm[0] = 1
        elif vm[0] < 0:
            vm[0] = 0
        if vm[1] > 1:
            vm[1] = 1
        elif vm[1] < 0:
            vm[1] = 0
        cliente.valvulas['valvula1'].set_value(vm[0])
        cliente.valvulas['valvula2'].set_value(vm[1])
        #ACTUALIZAR ERRORES
        h_error[5] = h_error[4]
        h_error[4] = h_error[3]
        h_error[2] = h_error[1]
        h_error[1] = h_error[0]        
    else:
        # VARIACIÓN DE VOLTAJE
        if state1 == "SV1":
            if vm[0] <= (1 - sensi):
                vm[0] += sensi
                cliente.valvulas['valvula1'].set_value(vm[0])
        elif state1 == "BV1":
            if vm[0] >= sensi:
                vm[0] -= sensi
                cliente.valvulas['valvula1'].set_value(vm[0])
        elif state1 == "SV2":
            if vm[1] <= (1 - sensi):
                vm[1] += sensi
                cliente.valvulas['valvula2'].set_value(vm[1])
        elif state1 == "BV2":
            if vm[1] >= sensi:
                vm[1] -= sensi
                cliente.valvulas['valvula2'].set_value(vm[1])
        # VARIACIÓN DE RAZONES
        elif state1 == "SF1":
            if vm[2] <= (1 - sensi):
                vm[2] += sensi
                cliente.razones['razon1'].set_value(vm[2])
        elif state1 == "BF1":
            if vm[2] >= sensi:
                vm[2] -= sensi
                cliente.razones['razon1'].set_value(vm[2])
        elif state1 == "SF2":
            if vm[3] <= (1 - sensi):
                vm[3] += sensi
                cliente.razones['razon2'].set_value(vm[3])
        elif state1 == "BF2":
            if vm[3] >= sensi:
                vm[3] -= sensi
                cliente.razones['razon2'].set_value(vm[3])
        state1 = " "


if __name__ == '__main__':
    cliente = Cliente("opc.tcp://localhost:4840/freeopcua/server/", suscribir_eventos=True,
                      SubHandler=SubHandler)
    cliente.conectar()
    Inicio()

    while True:
        Obtener()
        Eventos()
        Control()
        Interfaz(state, vc, temp, h_ref, pid, vm, programa_evento)
