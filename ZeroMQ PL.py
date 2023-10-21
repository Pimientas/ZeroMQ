import zmq

context = zmq.Context()

# Establecer la conexión con el socket
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Aquí debes usar la dirección y el puerto correctos

# Enviar un mensaje al socket
message = "start"  # Puedes personalizar el mensaje según tus necesidades
socket.send_string(message)

# Esperar la respuesta del socket si es necesario
response = socket.recv_string()
print("Respuesta recibida: ", response)

# Cerrar la conexión
socket.close()
context.term()
