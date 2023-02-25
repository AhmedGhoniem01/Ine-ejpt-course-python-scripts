import socket, os, platform

SRV_ADDR = "127.0.0.1"
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SRV_ADDR, PORT))
s.listen(1)
print(f"Target machine is listening on port {PORT}...")

connection, address = s.accept()

while(1):
    try:
        data = connection.recv(1024).decode("utf-8")
    except:
        continue

    if(data == "0"):
        print("Connection is to be aborted...")
        connection.close()
    elif(data == "1"):
        print("Getting operating system info: ")
        info = platform.platform() + " " + platform.machine()
        connection.sendall(info.encode("utf-8"))
    elif(data == "2"):
        path = connection.recv(1024).decode("utf-8")
        print("Getting path content: ")
        try:
            pathContents = os.listdir(path)
            toSend = ""
            for file in pathContents:
                toSend += (file + ",")
        except:
            toSend = "Wrong Path"
        connection.sendall(toSend.encode("utf-8"))




