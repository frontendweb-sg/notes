import socket


def client():
    # Create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # host ip
    port = 12345
    host = socket.gethostbyname(socket.gethostname())

    # connect
    client_socket.connect((host, port))
    print(f"Client connected on: {host}:{port}")

    while True:
        # send id to the server
        print("Fetch post")
        id = int(input("enter post id: "))
        if id <= 0 and id >= 101:
            print("Wrong id, thanks you")
            client_socket.close()
            break
        client_socket.send(str(id).encode())

        # receive data from the server
        res = client_socket.recv(1024).decode()
        if not res:
            client_socket.close()
            break
        print(res)

    client_socket.close()


if __name__ == "__main__":
    client()
