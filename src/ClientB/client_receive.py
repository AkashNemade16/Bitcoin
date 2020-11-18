from socket import *

ClientReceivePortA = 30000
ClientSocket = socket(AF_INET, SOCK_DGRAM)
ClientSocket.bind(('', ClientReceivePortA))
print('The server is ready to receive')
accounts = ["A0000001", "A0000002"]
while 1:
    message, clientAddress = ClientSocket.recvfrom(2048)
    modifiedMessage = message.decode()
    print(modifiedMessage)


    if len(modifiedMessage) == 24:
        #To check whether client is payer or payee
        trans = modifiedMessage
        payer = trans[0:8]
        payee = trans[8:16]
        amount = trans[16:24]

        with open("Unconfirmed_T", 'r+') as uf:
            ut = uf.read().splitlines()
            # check if account is payer
            if payer in accounts:
                # It makes sure that the Tx is available in its Unconfirmed_T. txt
                if trans in ut:
                    ut.remove(trans)

                    uf.seek(0)
                    uf.truncate()

                    for tf in ut:
                        tf = tf + '\n'
                        uf.write(tf)
                        # Appends confirmed transaction to Confirmed_T
                    with open("Confirmed_T", 'a') as Confirmed_File:
                        Confirmed_File.write(trans + '\n')

                        # Reduces Confirmed Balance of payer by Tx amount + Tx fee
                    with open("balance", 'r+') as Balance_File:
                        cf = Balance_File.read().splitlines()
                        Balance_File.seek(0)
                        Balance_File.truncate()
                        for balanceLine in cf:
                            balanceLine = balanceLine.split(":")
                            if balanceLine[0] == payer:
                                balanceLine[2] = "{:08x}".format(int(balanceLine[2], 16) - int(amount, 16) - 2)

                            Balance_File.write(":".join(balanceLine) + '\n')

            elif payee in accounts:
                # Appends confirmed transaction to Confirmed_T
                with open("Confirmed_T", 'a') as Confirmed_File:
                    Confirmed_File.write(trans + '\n')
                with open("balance", 'r+') as Balance_File:
                    confirmedBalances = Balance_File.read().splitlines()
                    Balance_File.seek(0)
                    Balance_File.truncate()
                    for balanceLine in confirmedBalances:
                        balanceLine = balanceLine.split(":")
                        if balanceLine[0] == payee:
                            balanceLine[1] = "{:08x}".format(int(balanceLine[1], 16) + int(amount, 16))
                            balanceLine[2] = "{:08x}".format(int(balanceLine[2], 16) + int(amount, 16))

                        Balance_File.write(":".join(balanceLine) + '\n')

    else:
        eval(modifiedMessage)
