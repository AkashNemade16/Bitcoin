from socket import *

uinitial_balance = int(1000)
cinitial_balance = int(1000)
aer = hex(uinitial_balance)
aer1 = hex(cinitial_balance)
with open('balance', 'w') as g:
    g.writelines("A0000001: " + aer + " : " + aer1 + "\n")
    g.writelines("A0000002: " + aer + " : " + aer1)

while 1:
    choice = input("""
          1:Enter a new transaction.
          2:The current balance for each account.
          3:Print the unconfirmed transactions.
          4:Print the last X number of confirmed transactions (either as a Payee or a Payer).
          5:Print the blockchain.

          Please enter your choice:""")

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

    amount = input("Enter the amount of payment in decimal:")
    i_amount = int(amount)
    tx_amount = hex(i_amount)
    tx_fee = 2

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
            w.write("balance : " + tx_amount + "\n")

        severName = 'localhost'
        serverPort = 10000
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        message = tx_amount
        clientSocket.sendto(message.encode(), (severName, serverPort))
        # modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # print(modifiedMessage)
        # clientSocket.close()
