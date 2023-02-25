import socket

SRV_ADDR= input("Enter the server address: ")
SRV_PORT = int(input("enter the server port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))
print("Connection established")

def print_menu():
    print("""\n\n
    0)Close the connection
    1)Get target os info
    2)Get target path contents""")

print_menu()

while(1):
    message = input("Enter option: ")
    
    if(message == "0"):
        s.sendall(message.encode("utf-8"))
        s.close()
        break
    elif(message == "1"):
        s.sendall(message.encode("utf-8"))
        data = s.recv(1024)
        if not data: break
        print("Message received: " + data.decode("utf-8"))
    elif(message == "2"):
        s.sendall(message.encode("utf-8"))
        path = input("Enter the required path: ")
        s.sendall(path.encode("utf-8"))
        data = s.recv(1024).decode("utf-8").split(",")
        if not data: break
        print("Message received: " + data)
        
    print_menu()
