import threading
import globals


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
        globals.info_evento = (True, event)
