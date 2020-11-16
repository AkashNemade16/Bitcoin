from socket import *

turn = 1
initial_balance = 0
initial_balance_hex = hex(initial_balance)

serverPort2 = 11000
serverPort1 = 20000
serverPort = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverName = 'localhost'
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print(modifiedMessage)
    serverSocket.sendto(modifiedMessage.encode(), (serverName, serverPort1))
    serverSocket.sendto(modifiedMessage.encode(), (serverName, serverPort2))
