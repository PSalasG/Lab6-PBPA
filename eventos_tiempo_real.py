import time
import random

class EventManager:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def unsubscribe(self, event, callback):
        if event in self.subscribers and callback in self.subscribers[event]:
            self.subscribers[event].remove(callback)

    def notify(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()
            self.event_manager.notify("cambios", self.data) # El RealTimeDataManager utiliza el método de notificar del EventManager.

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

# Función que será callback para imprimir los cambios.
def cambios_temp_humedad(data):
    print(f"Datos en tiempo real actualizados: {data}")

# Se crea la instancia de RealTimeDataManager y se suscribe la función callback.a
admin_eventos = RealTimeDataManager()
admin_eventos.event_manager.subscribe("cambios", cambios_temp_humedad)

# Actualizaciones en tiempo real en segundo plano
import threading
update_thread = threading.Thread(target=admin_eventos.start_real_time_updates)
update_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")