import socket

TCP_IP = "172.21.16.180"
TCP_PORT = 6781

BUFFER_SIZE = 1024

num1 = input("Digite a mensagem a ser passada ao servidor: ")
num1 = num1.encode()

num2 = input("Digite a mensagem a ser passada ao servidor: ")
num2 = num2.encode()

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((TCP_IP, TCP_PORT))
clientsocket.send(num1)
clientsocket.send(num2)

data = clientsocket.recv(BUFFER_SIZE).decode()

clientsocket.close()

print("Mensagem recebida: ", data)