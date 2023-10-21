import zmq
import time

print("Configurando contexto ZeroMQ")
context = zmq.Context()

print("Creando socket")
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Estado inicial de la lavadora
is_running = False

# Esperar y manejar los comandos
while True:
    print("Esperando mensajes...")
    message = socket.recv_string()
    print("Comando recibido: " + message)
    if message == "start":
        if not is_running:
            print("Iniciando la lavadora")
            is_running = True
            # Simulación de lavado por 10 segundos
            time.sleep(10)
            print("Lavado completado")
            is_running = False
            socket.send_string("Lavado completado")
        else:
            print("La lavadora ya está en funcionamiento, espera a que termine.")
            socket.send_string("Lavadora en uso, espera a que termine.")
    elif message == "stop":
        print("Deteniendo la lavadora")
        is_running = False
        socket.send_string("Lavadora detenida")
