import socket

UDP_IP = ""
UDP_PORT = 6789

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind((UDP_IP, UDP_PORT))

while True:
    data, address = serversocket.recvfrom(1024)
    print("Mensagem recebida: ", data.decode())