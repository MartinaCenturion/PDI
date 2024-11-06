import socket
import threading

# Configuración del servidor
server_ip = '127.0.0.1'
server_port = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen()

clients = []
nicknames = []

# Transmitir mensajes a todos los clientes conectados
def broadcast(message):
    for client in clients:
        client.send(message)

# Manejo de los clientes conectados
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} ha salido del chat.'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Aceptar nuevas conexiones
def receive():
    while True:
        client, address = server.accept()
        print(f"Conectado a {str(address)}")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"El apodo del cliente es {nickname}")
        broadcast(f"{nickname} se ha unido al chat.".encode('utf-8'))
        client.send("Conectado al servidor.".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Servidor corriendo...")
receive()



