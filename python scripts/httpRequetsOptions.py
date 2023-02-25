import http.client

ipAddress = input("Enter ip address: ")
Port = Ip_Address = input("Enter port number: ")

try:
    connection = http.client.HTTPConnection(ipAddress, Port)
    print("Sending options request...")
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    print("Allowed methods are: " + response.getheader('allow'))
    connection.close()
except:
    print("Request failed...")
