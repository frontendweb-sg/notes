# import socket


# def client():
#     # Get the host name (as both server and client code are running on your PC)
#     host = socket.gethostname()
#     # Define the server's port number to interact with
#     port = 21042
#    # Create a socket object
#     client_socket = socket.socket()
#     # Connect to the server by specifying the hostname and port number
#     client_socket.connect((host, port))
#     # Prompt the user for input
#     message = input("Enter your message (Type 'bye' to exit): ")
#     while message.lower().strip() != "bye":
#         # Send the message to the server
#         client_socket.send(message.encode())
#         # Receive a response from the server
#         data = client_socket.recv(1024).decode()
#         # Display the received message from the server
#         print("Received from server: " + data)
#         # Prompt for the next message
#         message = input("Enter your message (Type 'bye' to exit): ")
#     # Close the connection
#     client_socket.close()


# if __name__ == "__main__":
#     client()

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
# print(f"hostname: {hostname}, hostip: {hostip}")


# bind our new socket to a tuple
s = server_socket.bind((hostip, 12345))

# listen
server_socket.listen()

# listen forever
while True:
    client_socket, client_address = server_socket.accept()
    print(f"client: {client_socket}, and connected to: {client_address}")

    client_socket.send("You are connected!".encode("utf-8"))

    server_socket.close()
