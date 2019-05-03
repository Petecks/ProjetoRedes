import socket


def server_UDP(FILENAME = "README.txt", host = 'localhost', port= 10000):

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    server_address = (host, port)
    sock.bind(server_address)
    checksum = []

    F = open("response" + FILENAME, "wb")
    while True:
        data, address = sock.recvfrom(65500)
        cs, address2 = sock.recvfrom(65500)
        checksum.append(int.from_bytes(cs, "big"))

        if data:
            sock.sendto(data, address)
        if data == bytes("EOF", 'utf-8'): break
        F.write(data)
    checksum.pop()
    F.close()
    Fcs = open("responsecssv", "w")
    for item in checksum:
        Fcs.write("%s\n" % item)
    Fcs.close()

def server_TCP():
    print("nao implementado")