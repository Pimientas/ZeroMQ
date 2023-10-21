import paho.mqtt.client as mqtt

# Configuración del cliente MQTT
client = mqtt.Client()
client.connect("localhost", 1883, 60)

# Publicar un mensaje en un tópico
topic = "lavadora/control"
message = "start"
client.publish(topic, message)

# Desconectar el cliente MQTT
client.disconnect()

