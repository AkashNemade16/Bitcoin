from socket import *

turn = 1
initial_balance = 0
initial_balance_hex = hex(initial_balance)

serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

