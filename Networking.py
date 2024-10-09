import socket

#create a socket object
mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the server at py4inf.com on port 80(HTTP)
mysock.connect(('data.pr4e.org', 80))

#send a GET request to fetch the reo.txt file
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Receive and print the data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

#Close the socket
mysock.close()