import socket


def server():
    # Get the hostname of the server
    host = socket.gethostname()

    # Specify the port to listen on
    port = 21042

    # Create a socket object
    s = socket.socket()

    # Bind the socket to the host and port
    s.bind((host, port))

    # Listen for incoming connections, allowing up to 2 clients in the queue
    s.listen(2)

    # Accept an incoming connection
    c, address = s.accept()
    print(f"Connected to: {address}")

    while True:
        # Receive data from the client (up to 1024 bytes) and decode it
        data = c.recv(1024).decode()

        # If no data is received, break the loop
        if not data:
            break
        print(f"Received from client: {data}")

        # Get user input and send it to the client after encoding
        response = input("Enter response to send to client: ")
        c.send(response.encode())
    # Close the client connection
    c.close()


if __name__ == "__main__":
    # Start the server
    # server()
    print(socket.HVSOCKET_ADDRESS_FLAG_PASSTHRU)
    print(socket.AF_APPLETALK)
    print(socket.AF_BLUETOOTH)
    print(socket.AF_DECnet)
    print(socket.AF_INET)
    print(socket.AF_INET6)
    print(socket.AF_IPX)
    print(socket.AF_IRDA)
    print(socket.TCP_NODELAY)
