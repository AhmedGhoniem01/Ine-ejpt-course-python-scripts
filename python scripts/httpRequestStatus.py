import http.client

ipAddress = input("Enter ip address: ")
Port = Ip_Address = input("Enter port number: ")
url = input("Enter url address: ")


try:
    connection = http.client.HTTPConnection(ipAddress, Port)
    print("Sending request...")
    connection.request('GET', url)
    response = connection.getresponse()
    print("Response status code: " + response.status)
    connection.close()
except:
    print("Request failed...")
