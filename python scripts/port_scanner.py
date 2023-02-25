import socket
Target = input("Enter Target address: ")
Port_Range = input("Enter the range of ports to scan [Ex: 100-300]: ")

low_port =  int(Port_Range.split("-")[0])
high_port= int(Port_Range.split("-")[1])
print("Connection to the server address "+Target+ " will be tested on the port range from: "+str(low_port)+" to "+str(high_port))

for port in range(low_port, high_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((Target, port))
    if status == 0:
        print("Port "+str(port)+" is open on the target")
    else:
        print("Port "+str(port)+" is closed on the target")
s.close()
#

