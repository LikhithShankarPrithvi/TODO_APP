# server.py
import socket
import threading

clients = []
nicknames = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except Exception as e:
                print(f"Error sending message: {e}")
                client.close()
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except Exception as e:
            index = clients.index(client_socket)
            clients.remove(client_socket)
            client_socket.close()
            nickname = nicknames.pop(index)
            print(f"{nickname} disconnected")
            broadcast(f"{nickname} has left the chat!".encode('utf-8'), client_socket)
            break

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen()
    print("Server is listening on port 12345...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connected with {address}")

        client_socket.send("NICK".encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client_socket)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'), client_socket)
        client_socket.send("Connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()

