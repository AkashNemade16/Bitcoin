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
  
  Please enter your choice:""")


def new_transaction():
    pass


def current_balance():
    pass


def unconfirmed_transactions():
    pass


def confirmed_transactions():
    pass


def blockchain():
    pass


if choice == "A":
    new_transaction()
elif choice == "B":
    current_balance()
elif choice == "B":
    unconfirmed_transactions()
elif choice == "B":
    confirmed_transactions()
elif choice == "B":
    blockchain()