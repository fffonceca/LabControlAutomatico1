from interfaz import Interfaz
from Libreria.cliente import Cliente


class Control():
    def __init__(self):
        self.pid = [[0, 0, 0], [0.1, 0.01, 0.02], [0.1, 0.01, 0.02], [0, 0, 0]]
        self.h_error = [0, 0, 0, 0, 0, 0]
        self.state1 = ""
        self.alturas = [0, 0, 0, 0]
        self.volt_razones = [0, 0, 0, 0]
        self.mouse_pos = [0, 0]
        self.windup = [0, 1, 0, 1]  # wi1, ws1, wi2, ws2

    def setear_variables(self, alturas, volt_razones):
        self.alturas = alturas
        self.volt_razones = volt_razones

    def actualizar(self, cliente: Cliente, interfaz: Interfaz):
        sensi = 0.05
        Ts = 0.01
        h_error = self.h_error
        pid = self.pid
        vm = self.volt_razones
        vc = self.alturas

        if(interfaz.modo == "A"):
            # CAMBIO DE REFERENCIA
            if self.state1 == "R":
                if 202 < self.mouse_pos[0] < 300 and 252 < self.mouse_pos[1] < 400:
                    interfaz.h_ref[0] = (self.mouse_pos[1] - 399) * (- 50 / 146)
                if 342 < self.mouse_pos[0] < 440 and 252 < self.mouse_pos[1] < 400:
                    interfaz.h_ref[1] = (self.mouse_pos[1] - 399) * (- 50 / 146)
                self.state1 = " "

            # DEFINICIÓN DE ERRORES
            h_error[0] = interfaz.h_ref[0] - vc[0]
            h_error[3] = interfaz.h_ref[1] - vc[1]

            # CONTROL PID
            (Kp1, Ki1, Kd1) = pid[0]
            (Kp2, Ki2, Kd2) = pid[1]
            (Kp3, Ki3, Kd3) = pid[2]
            (Kp4, Ki4, Kd4) = pid[3]

            vm[0] += Kp1*(h_error[0]-h_error[1]) + Ki1*Ts*h_error[0] +\
                Kd1*(h_error[0]-h_error[1]+h_error[2])/Ts
            vm[0] += Kp2*(h_error[3]-h_error[4]) + Ki2*Ts*h_error[3] +\
                Kd2*(h_error[3]-h_error[4]+h_error[5])/Ts
            vm[1] += Kp3*(h_error[0]-h_error[1]) + Ki3*Ts*h_error[0] +\
                Kd3*(h_error[0]-h_error[1]+h_error[2])/Ts
            vm[1] += Kp4*(h_error[3]-h_error[4]) + Ki4*Ts*h_error[3] +\
                Kd4*(h_error[3]-h_error[4]+h_error[5])/Ts

            # ANTI WINDUP
            if vm[0] > self.windup[1]:
                vm[0] = self.windup[1]
            elif vm[0] < self.windup[0]:
                vm[0] = self.windup[0]
            if vm[1] > self.windup[3]:
                vm[1] = self.windup[3]
            elif vm[1] < self.windup[2]:
                vm[1] = self.windup[2]
            cliente.valvulas['valvula1'].set_value(vm[0])
            cliente.valvulas['valvula2'].set_value(vm[1])

            # ACTUALIZAR ERRORES
            h_error[5] = h_error[4]
            h_error[4] = h_error[3]
            h_error[2] = h_error[1]
            h_error[1] = h_error[0]
            self.h_error = h_error

        else:
            # VARIACIÓN DE VOLTAJE
            if self.state1 == "SV1":
                if vm[0] <= (1 - sensi):
                    vm[0] += sensi
                    cliente.valvulas['valvula1'].set_value(vm[0])
                else:
                    vm[0] = 1
                    cliente.valvulas['valvula1'].set_value(vm[0])
            elif self.state1 == "BV1":
                if vm[0] >= sensi:
                    vm[0] -= sensi
                    cliente.valvulas['valvula1'].set_value(vm[0])
                else:
                    vm[0] = 0
                    cliente.valvulas['valvula1'].set_value(vm[0])
            elif self.state1 == "SV2":
                if vm[1] <= (1 - sensi):
                    vm[1] += sensi
                    cliente.valvulas['valvula2'].set_value(vm[1])
                else:
                    vm[1] = 1
                    cliente.valvulas['valvula2'].set_value(vm[1])
            elif self.state1 == "BV2":
                if vm[1] >= sensi:
                    vm[1] -= sensi
                    cliente.valvulas['valvula2'].set_value(vm[1])
                else:
                    vm[1] = 0
                    cliente.valvulas['valvula2'].set_value(vm[1])

        # VARIACIÓN DE RAZONES
        if self.state1 == "SF1":
            if vm[2] <= (1 - sensi):
                vm[2] += sensi
                cliente.razones['razon1'].set_value(vm[2])
        elif self.state1 == "BF1":
            if vm[2] >= sensi:
                vm[2] -= sensi
                cliente.razones['razon1'].set_value(vm[2])
        elif self.state1 == "SF2":
            if vm[3] <= (1 - sensi):
                vm[3] += sensi
                cliente.razones['razon2'].set_value(vm[3])
        elif self.state1 == "BF2":
            if vm[3] >= sensi:
                vm[3] -= sensi
                cliente.razones['razon2'].set_value(vm[3])
        self.state1 = " "
        self.volt_razones = vm
