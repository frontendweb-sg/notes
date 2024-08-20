import socket
import requests


def fetch_data(id: int) -> dict:
    post = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    return post.json()


def server():

    # Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # host ip
    port = 12345
    host = socket.gethostbyname(socket.gethostname())

    # bind socket to host and port
    server_socket.bind((host, port))

    # listen
    server_socket.listen()
    print(f"server is running on \"{host}:{port}\"")

    # accept connection
    client_socket, client_addr = server_socket.accept()
    print(f"Client connect: {client_addr}")

    while True:
        print("Server is running...")

        # receive message from client
        id = int(client_socket.recv(1024).decode())
        print(f"id:{id}-{type(id)}")

        if not id or id <= 0 and id >= 100:
            print("client disconnected!")
            break

        # send message to client
        post = fetch_data(id)
        client_socket.send(str(post).encode())


if __name__ == "__main__":
    server()
