import socket
import threading

PORT = 8820

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(2)
(client_socket_1, client_adress_1) = server_socket.accept()
(client_socket_2, client_adress_2) = server_socket.accept()

def main():

    client_socket_1.send("A")
    client_socket_2.send("B")

    screen = threading.Thread(target=screen_shots)
    command = threading.Thread(target=commands)

    # screen.start()
    command.start()


def screen_shots():
    while True:
        image = client_socket_2.recv(9000)
        client_socket_1.send(image)


def commands():
    while True:
        command = client_socket_1.recv(9000)
        client_socket_2.send(command)

if __name__ == '__main__':
    main()