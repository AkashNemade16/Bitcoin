from socket import *

severName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input('Input lowercase sentence:')
# clientSocket.sendto(message.encode()(severName, serverPort))
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print(modifiedMessage.decode())
# clientSocket.close()


# initializing-balances
uinitial_balance = int(1000)
cinitial_balance = int(1000)
aer = hex(uinitial_balance)
aer1 = hex(cinitial_balance)
with open('balance', 'w') as g:
    g.writelines("A0000001: " + aer + " : " + aer1 + "\n")
    g.writelines("A0000002: " + aer + " : " + aer1)


choice = input("""
1:Enter a new transaction.
2:The current balance for each account.
3:Print the unconfirmed transactions.
4:Print the last X number of confirmed transactions (either as a Payee or a Payer).
5:Print the blockchain.

Please enter your choice:""")


def new_transaction():
    print("Select the payer:")
    choice_payer = input("""
1:A0000001
2:A0000002
           """)

    print("Select the payee:")
    choice_payee = input("""
1:B0000001
2:B0000002
            """)

    # converting the tx_amount into hex#
    amount = input("Enter the amount of payment in decimal:")
    i_amount = int(amount)
    tx_amount = hex(i_amount)


    # tx-fee
    tx_fee = hex(2)

    if choice_payer == "1":
        with open('balance', 'r') as t:
            f_content1 = t.readline()
            f_content2 = f_content1.split(":")
            var = f_content2[1]  # unconfirmed_balance = var

            tm = tx_amount + tx_fee

        if tm <= var:
            var -= tm
            with open('Unconfirmed_T', 'w') as w:
                w.write('h')


def current_balance():
    with open('balance', 'r') as f:
        f_content = f.readline()
        con = f_content.split(":")
        var = con[2]
        var1 = int(var, 16)
        final = str(var1)
        print("Account-1 : " + final)

        f_content = f.readline()
        con1 = f_content.split(":")
        var2 = con1[2]
        var3 = int(var2, 16)
        final1 = str(var3)
        print("Account-2 : " + final1)


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
