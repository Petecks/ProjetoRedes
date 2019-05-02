import socket


FILENAME = "test.png"
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
contents = []
checksum = []

F = open("response" + FILENAME, "ab")
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(65500)
    cs, address2 = sock.recvfrom(65500)
    checksum.append(int.from_bytes(cs,"big"))
    #contents.append(data)
    #print(contents)


    if data:
        sent = sock.sendto(data, address)
        #print('sent {} bytes back to {}'.format(
           # sent, address))
    if data == bytes("EOF", 'utf-8'): break
    F.write(data)
checksum.pop()
F.close()
print(checksum)