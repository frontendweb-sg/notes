# What is socket programming?

Socket programming is a communication between nodes (machine) over network.

A server is a software program that wait for client request and serve the incomming process, while a client is a requester of the service.

A client request resources from the server and the server respond to the server.

To establish, a connection between the `client` and the `server`. we create a `socket`
in each program and then connect both socket together.

`Basic Concepts:`

- `Socket:` An endpoint for sending or receiving data across a network.
- `Server:` Listening for incoming connections from clients.
- `Client:` Connects to the server to send and receive data.

**`Server:`**

```py
# server.py

import socket

# create server socket """OBJECT""" using socket(family, type, proto) method.
# socket.SOCK_STREAM :- Specify the type, this is default type
# socket.AF_INTER: Default socket family
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get machine hostname
host_name = socket.gethostname()

# get machine host id
host_ip = socket.gethostbyname(host_name)

# bind to a new connection
server_socket.bind((host_ip, 12345)) # 12345 it is a port number, you can choose any port number

# now listen the connection
server_socket.listen() # it will listen client request
```
