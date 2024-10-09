import socket
import threading


def receive(client_socket):
    while True:
        try:
            # receive data from the server
            res = client_socket.recv(1024).decode()
            if not res:
                client_socket.close()
                break
            print(res)
        except:
            break


def write(client_socket):
    while True:
        id = int(input("enter post id: "))
        if id <= 0 and id >= 101:
            print("Wrong id, thanks you")
            client_socket.close()
        client_socket.send(str(id).encode())


def start_client():
    # Create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # host ip
    port = 12345
    host = socket.gethostbyname(socket.gethostname())

    # connect
    client_socket.connect((host, port))
    print(f"Client connected on: {host}:{port}")

    thread1 = threading.Thread(target=receive, args=(client_socket,))
    thread1.start()

    thread2 = threading.Thread(target=write, args=(client_socket,))
    thread2.start()


if __name__ == "__main__":
    start_client()
