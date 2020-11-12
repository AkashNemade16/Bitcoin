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
1:Enter a new transaction.
2:The current balance for each account.
3:Print the unconfirmed transactions.
4:Print the last X number of confirmed transactions (either as a Payee or a Payer).
5:Print the blockchain.

Please enter your choice:""")


def display_functions():
    print("Select the payer:")
    choice_payer = input("""
1:A0000001
2:A0000002
       """)

    # if choice_payer == "1" or choice_payer == "2":
    print("Select the payee:")
    choice_payee = input("""
1:B0000001
2:B0000002
        """)
    amount = input("Enter the amount in decimal:")

    return choice_payer, choice_payee, amount


def new_transaction():
    display_functions()


def current_balance():
    with open('balance', 'r') as f:
        f_contents = f.readline()
        print("Account-1 "+f_contents[18:26])
        f_contents = f.readline()
        print("Account-2 "+f_contents[18:26])


def unconfirmed_transactions():
    pass


def confirmed_transactions():
    pass


def blockchain():
    pass


if choice == "1":
    new_transaction()
elif choice == "2":
    current_balance()
elif choice == "3":
    unconfirmed_transactions()
elif choice == "4":
    confirmed_transactions()
elif choice == "5":
    blockchain()
