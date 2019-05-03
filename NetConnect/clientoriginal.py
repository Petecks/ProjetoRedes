import socket

FILENAME = "test.png"

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message.  It will be repeated.'
fileend= "EOF"




def checksum(ip_header, size):
    cksum = 0
    pointer = 0

    # The main loop adds up each set of 2 bytes. They are first converted to strings and then concatenated
    # together, converted to integers, and then added to the sum.
    while size > 1:
        cksum += int((str("%02x" % (ip_header[pointer],)) + str("%02x" % (ip_header[pointer + 1],))), 16)
        size -= 2
        pointer += 2
    if size:  # This accounts for a situation where the header is odd
        cksum += ip_header[pointer]

    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >> 16)

    return (~cksum) & 0xFFFF

cs = []
try:
    f = open(FILENAME, "rb")
    content = f.read()
    content = bytes(content)

    # Send data
    while len(content):
        part_of = bytearray(content[:16375])
        content = bytearray(content[16375:])

        sent = sock.sendto(part_of, server_address)
        #msg = (checksum(part_of, len(part_of))).to_bytes(2, byteorder="big")
        #sock.sendto(msg, server_address)
        #cs.append(checksum(part_of, len(part_of)))
        data, server = sock.recvfrom(65500)

    sock.sendto(bytes(fileend,'utf-8'), server_address)
    #sock.sendto(bytes(fileend,'utf-8'), server_address)
finally:

    print('closing socket')
    sock.close()
    f.close()
    print(cs)