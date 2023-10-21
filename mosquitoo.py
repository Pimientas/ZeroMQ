import paho.mqtt.client as mqtt
import time

# Funciones de callback
def on_connect(client, userdata, flags, rc):
    print("Conectado con código de resultado " + str(rc))
    client.subscribe("lavadora/control")

def on_message(client, userdata, msg):
    global is_running
    message = msg.payload.decode()
    print("Comando recibido: " + message)
    if message == "start":
        if not is_running:
            print("Iniciando la lavadora")
            is_running = True
            # Simulación de lavado por 10 segundos
            time.sleep(10)
            print("Lavado completado")
            is_running = False
        else:
            print("La lavadora ya está en funcionamiento, espera a que termine.")

# Configuración del cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conexión al broker MQTT local
client.connect("localhost", 1883, 60)

print("Conexión exitosa")

# Estado inicial de la lavadora
is_running = False

# Mantener la conexión en un bucle infinito
print("Iniciando el bucle de MQTT")
client.loop_forever()
