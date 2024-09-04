import socket
import threading
import requests
import json

clients = []


def fetch_data(id: int) -> dict:
    post = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    return post.json()


def broadcast(id: int, client_socket):
    try:
        for client in clients:
            # if client != client_socket:
            post = fetch_data(id)
            client.send(str(post).encode())
            print(f"data sent to client")
            print(f"total connection: {len(clients)}")
    except socket.error:
        print("Broadcast: something went wrong")
        client_socket.close()
        clients.remove(client_socket)


def handle_client(client_socket):
    print(f"thread: {threading.current_thread()}")
    while True:
        try:
            id = int(client_socket.recv(1024).decode())

            if id <= 0 and id >= 101:
                print("Wrong id, thanks you")
                clients.remove(client_socket)
                client_socket.close()
                break
            broadcast(id, client_socket)
        except socket.error:
            print("Broadcast: something went wrong")
            client_socket.close()
            clients.remove(client_socket)
            break


def start_server():
    # create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # host
    port = 12345
    host = socket.gethostbyname(socket.gethostname())

    # bind host to socket
    server_socket.bind((host, port))

    # listen
    server_socket.listen()
    print(f"server is running on {host}:{port}")

    while True:
        print("server is running...")
        client_socket, client_addr = server_socket.accept()
        print(f"client connected: {client_addr}")

        # if client_socket not in clients:
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

        server_socket.close()


if __name__ == "__main__":
    start_server()
