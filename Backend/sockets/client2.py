
# client.py
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print("Disconnected from the server.")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input()
        if message.lower() == '/exit':
            client_socket.close()
            break
        else:
            client_socket.send(message.encode('utf-8'))

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    response = client_socket.recv(1024).decode('utf-8')
    if response == "NICK":
        nickname = input("Enter your nickname: ")
        client_socket.send(nickname.encode('utf-8'))

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
