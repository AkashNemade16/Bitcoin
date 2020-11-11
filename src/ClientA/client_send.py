from socket import *
severName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input('Input lowercase sentence:')
# clientSocket.sendto(message.encode()(severName, serverPort))
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print(modifiedMessage.decode())
# clientSocket.close()

choice = input("""
  1:"Enter a new transaction."
  2:"The current balance for each account."
  3:"Print the unconfirmed transactions."
  4:"Print the last X number of confirmed transactions (either as a Payee or a Payer)."
  5:"Print the blockchain."
""")
