import socket

SRV_ADDR = input("Enter the server address: ")
SRV_PORT = int(input("Eneter the port: "))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SRV_ADDR, SRV_PORT))
server_socket.listen(1)

print("Server Started... Waiting for requests")
connection, address = server_socket.accept()
# print("Client connected with address: " + address)

while(1):
    data = connection.recv(1024)
    if not data:
        break
    print("Data recieved: " + data.decode("utf-8"))
    replyMessage = "Message successfully recieved...\n" 
    connection.sendall(replyMessage.encode("utf-8"))
    
connection.close()



