import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)

client_socket.connect((hostip, 12345))

message = client_socket.recv(1024)

print(message.decode("utf-8"))


client_socket.close()
