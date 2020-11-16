from socket import *

turn = 1
initial_balance = 0
initial_balance_hex = hex(initial_balance)

serverPort2 = 11000  # F2
serverPort1 = 20000  # client-recieve
serverPort = 10000 #F1
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverName = 'localhost'
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print(modifiedMessage)
    clientA = modifiedMessage
    # serverSocket.sendto(clientA.encode(), (serverName, serverPort1))
    serverSocket.sendto(clientA.encode(), (serverName, serverPort2))

    message1, clientAddress1 = serverSocket.recvfrom(2048)
    msg = message1.decode()
    print(msg)

    # if clientA == modifiedMessage:  # receive tx and appending to temp_t.txt
    #     with open('Temp_T', '+a') as w:
    #         w.write("Tx: " + clientA + "\n")
    #
    # with open('Temp_T', 'r') as f:
    #     counter = 0
    #     f_content = f.read()
    #     coList = f_content.split("\n")
    #     for i in coList:
    #         if i:
    #             counter += 1
    #     # print(counter)
    # if counter == 4:
    #     turn += 1
    # if (turn % 2) == 1:
    #     serverSocket.close()
    #     break

