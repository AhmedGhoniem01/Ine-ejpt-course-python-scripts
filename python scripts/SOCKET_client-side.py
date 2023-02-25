import socket

SRV_ADDR = input("Enter the server address to connect to: ")
SRV_PORT = int(input("Eneter the port of the server: "))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SRV_ADDR, SRV_PORT))
print("Connection established...\n")

message= input("Enter a message to send: ")
while(message.strip().lower() != "end"):
    client_socket.send(message.encode("utf-8"))
    message= input("Enter a message to send: ")

client_socket.close()