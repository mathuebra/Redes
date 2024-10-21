import socket

UDP_IP = "172.21.16.180"
UDP_PORT = 6789

message = input("Digite a mensagem a ser passada ao servidor: ")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientsocket.sendto(message, (UDP_IP, UDP_PORT))