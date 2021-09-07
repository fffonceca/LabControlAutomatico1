import threading
import globals


def funcion_handler(node, val):
    key = node.get_parent().get_display_name().Text
    variable = node.get_display_name().Text
    if 'Tanque' in key:
        pos = int(key[-1]) - 1
        if variable == 'T':
            globals.interfaz.temp[pos] = val
        elif variable == 'h':
            globals.interfaz.alturas[pos] = val
            globals.control.alturas[pos] = val
        else:
            print("No se entiende variable")
    elif 'Razon' in key:
        pos = int(key[-1]) - 1
        globals.interfaz.razones[pos] = val
        print(key, variable, val)
    elif 'Valvula' in key:
        pos = int(key[-1]) - 1
        globals.interfaz.voltajes[pos] = val
        print(key, variable, val)
    else:
        print(key, variable, val)


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
        globals.info_evento = (True, event)
