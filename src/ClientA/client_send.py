from socket import *


class ClientSend:

    def __init__(self, tx_amount):
        self.tx_amount = tx_amount

    uinitial_balance = int(1000)
    cinitial_balance = int(1000)
    aer = '{:08x}'.format(uinitial_balance)
    aer1 = '{:08x}'.format(cinitial_balance)
    with open('balance', 'w') as g:
        g.writelines("A0000001: " + aer + " : " + aer1 + "\n")
        g.writelines("A0000002: " + aer + " : " + aer1)

    def new_transaction(self):

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
        amount = input("Enter the amount of payment in decimal:\n")
        print("Tx: " + choice_payer + " pays " + choice_payee + " the amount of " + amount+ " BC")
        i_amount = int(amount)
        self.tx_amount = '{:08x}'.format(i_amount)

        # tx-fee
        tx_fee = 2
        # for account 1
        if choice_payer == "1":

            with open('balance', 'r') as t:
                f_content1 = t.readline()
                f_content2 = f_content1.split(":")
                var = f_content2[1]  # unconfirmed_balance
                var1 = int(var, 16)
                tm = i_amount + tx_fee

            if tm <= var1:
                var2 = var1 - tm
                var3 = hex(var2)  # unconfirmed_balance - (tx_amount+tx_fee)

            with open('Unconfirmed_T', 'a+') as w:
                # for i in range(0, 3):
                w.write("A1-balance : " + self.tx_amount + "\n")
            self.socket()
        # with open('E:\Bitcoin-Project\src\F1\Temp_T', 'w') as l:
        #     l.write(tx_amount)  # sending tx to full node f1
        # return self.tx_amount

        # for account 2
        if choice_payer == "2":
            with open('balance', 'r') as t:
                f_content1 = t.readline()
                f_content1 = t.readline()
                f_content2 = f_content1.split(":")
                var = f_content2[1]  # unconfirmed_balance
                var1 = int(var, 16)
                tm = i_amount + tx_fee

            if tm <= var1:
                var2 = var1 - tm
                var3 = hex(var2)  # unconfirmed_balance - (tx_amount+tx_fee)

            with open('Unconfirmed_T', 'a+') as w:
                # for i in range(0, 3):
                w.write("A2-balance : " + self.tx_amount + "\n")
            self.socket()

    def current_balance(self):
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

    def unconfirmed_transactions(self):
        with open('Unconfirmed_T', 'r') as t:
            f = t.read()
            print(f)

    def confirmed_transactions(self):
        pass

    def blockchain(self):
        pass

    def socket(self):

        severName = 'localhost'
        serverPort = 10000
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        message = self.tx_amount
        clientSocket.sendto(message.encode(), (severName, serverPort))
        clientSocket.close()


while 1:

    choice = input("""
1:Enter a new transaction.
2:The current balance for each account.
3:Print the unconfirmed transactions.
4:Print the last X number of confirmed transactions (either as a Payee or a Payer).
5:Print the blockchain.

Please enter your choice:""")
    Object = ClientSend('')
    if choice == "1":
        Object.new_transaction()
    elif choice == "2":
        Object.current_balance()
    elif choice == "3":
        Object.unconfirmed_transactions()
    elif choice == "4":
        Object.confirmed_transactions()
    elif choice == "5":
        Object.blockchain()
    else:
        break
