from socket import *
import hashlib

turn = 2
initial_balance = 0
initial_balance_hex = hex(initial_balance)
serverName = 'localhost'
clientPortB = 11001#client send B
serverPort1 = 10000  # F1
serverPort = 11000  # F2
serverPort2 = 30000  # client_receive B
serverSocketF2 = socket(AF_INET, SOCK_DGRAM)
serverSocketF2.bind(('', serverPort))
print('The server is ready to receive')

with open("Temp_T", "w") as File:
    File.seek(0)
    File.truncate()

with open("Blockchain", "w") as File:
    File.seek(0)
    File.truncate()

while 1:
    message, clientAddress = serverSocketF2.recvfrom(2048)
    modifiedMessage = message.decode()

    if clientAddress[1] == clientPortB and len(message.decode()) == 24:
        # recieving the tx
        tx = modifiedMessage
        print("tx received: " + tx)
        serverSocketF2.sendto(tx.encode(), (serverName, serverPort1))
        with open('Temp_T', '+a') as w:
            w.write(tx.lstrip() + "\n")

            # to check number of transactions
        with open('Temp_T', 'r') as f:
            counter = 0
            f_content = f.read()
            coList = f_content.split("\n")
            for i in coList:
                if i:
                    counter += 1

        if counter == 4:
            turn += 1
            if (turn % 2) == 1:
                pass
            else:
                # Extract 4 Tx from Temp_T

                with open("Temp_T", "r+") as t:
                    txs = t.read().splitlines()
                    t.seek(0)
                    t.truncate()
                counter = 0  # for number of transactions

                with open('Temp_T', 'r') as r:
                    f_content = r.read()  # to read all the tx's
                    f_content1 = r.readline()
                    f_content2 = r.readline()
                    f_content3 = r.readline()
                    f_content4 = r.readline()


                def hash(mes):
                    m = hashlib.sha256()
                    m.update(mes.encode("utf-8"))
                    m.hexdigest()
                    return m


                a = hash(mes=f_content1)
                # print(a)
                b = hash(mes=f_content2)
                # print(b)
                c = hash(mes=f_content3)
                # print(c)
                d = hash(mes=f_content4)
                # print(d)

                ab = str(a) + str(b)
                ab1 = hash(ab)
                # print(ab1)

                cd = str(c) + str(d)
                cd1 = hash(cd)
                # print(cd1)

                abcd = str(ab1) + str(cd1)
                abcd1 = hash(abcd)  # merkle root
                # print(abcd1)

                # mining fee
                balance = 0
                balance = balance + 38
                # mine the block
                lastblockhash = str().zfill(32)
                hashHandler = hashlib.sha256()
                nonce = 0

                while True:
                    block_header = str(nonce) + lastblockhash + abcd1.__str__()
                    hashHandler.update(block_header.encode("utf-8"))
                    hashValue = hashHandler.hexdigest()

                    nounceFound = True
                    for i in range(4):
                        if hashValue[i] != '0':
                            nounceFound = False
                    if nounceFound:
                        print('nonce:{0}, hash:{1}'.format(nonce, hashValue))
                        break
                    else:
                        nonce = nonce + 1

                header = "{:08x}".format(nonce) + lastblockhash + abcd1.__str__()
                body = f_content1 + f_content2 + f_content3 + f_content4
                block = header + body

                with open('Blockchain', 'a+') as g:
                    g.writelines(block + "\n")

                # send tx to clientreceive for confirmation
                for transm in f_content:
                    serverSocketF2.sendto(transm.encode(), (serverName, serverPort2))

                # sending block to full node f1
                serverSocketF2.sendto(block.encode(), (serverName, serverPort1))
                print("block: " + block)

    elif clientAddress[1] == clientPortB and message.decode() == "blockchain request":
        print("sending blockchain")
        with open('Blockchain', 'r') as b:
            blockchain = b.readlines()
            for block in blockchain:
                serverSocketF2.sendto(block.encode(), (serverName, serverPort2))
        serverSocketF2.sendto('Blockchain sent'.encode(), (serverName, serverPort2))

    # checking if the request is from F1
    elif clientAddress[1] == serverPort1:
        if len(modifiedMessage) == 232:
            block = modifiedMessage
            hashblock = hashlib.sha256()
            hashblock.update(block.encode("utf-8"))
            lastblockhash = hashblock.hexdigest()
            print("hash of previous block: " + lastblockhash)

            # appending block to blockchain.txt
            with open("Blockchain", 'a+') as bl:
                bl.write(block + "\n")

            # Remove the 4 Tx of the block from Temp_T.txt

            with open("Temp_T.txt", "r+") as rem:
                txs = rem.read().splitlines()
                rem.seek(0)
                rem.truncate()

            counter = 0
            # Check the 4 Tx of the block and send the Tx where its client is a Payer or Payee to
            # the client. The purpose is to let the client know these Tx are confirmed.
            for tx in txs:
                serverSocketF2.sendto(tx.encode(), (serverName, serverPort2))

        else:
            # Receiving a Transaction
            txs = modifiedMessage
            print("Received Transaction: " + txs)

            with open('Temp_T', '+a') as w:
                w.write(txs.lstrip() + "\n")

                # to check number of transactions
            with open('Temp_T', 'r') as f:
                counter = 0
                f_content = f.read()
                coList = f_content.split("\n")
                for i in coList:
                    if i:
                        counter += 1

            if counter == 4:
                turn += 1
                if (turn % 2) == 1:
                    pass
                else:
                    # Extract 4 Tx from Temp_T

                    with open("Temp_T", "r+") as t:
                        txs = t.read().splitlines()
                        t.seek(0)
                        t.truncate()
                    counter = 0  # for number of transactions

                    with open('Temp_T', 'r') as r:
                        f_content = r.read()  # to read all the tx's
                        f_content1 = r.readline()
                        f_content2 = r.readline()
                        f_content3 = r.readline()
                        f_content4 = r.readline()


                    def hash(mes):
                        m = hashlib.sha256()
                        m.update(mes.encode("utf-8"))
                        m.hexdigest()
                        return m


                    a = hash(mes=f_content1)
                    # print(a)
                    b = hash(mes=f_content2)
                    # print(b)
                    c = hash(mes=f_content3)
                    # print(c)
                    d = hash(mes=f_content4)
                    # print(d)

                    ab = str(a) + str(b)
                    ab1 = hash(ab)
                    # print(ab1)

                    cd = str(c) + str(d)
                    cd1 = hash(cd)
                    # print(cd1)

                    abcd = str(ab1) + str(cd1)
                    abcd1 = hash(abcd)  # merkle root
                    # print(abcd1)

                    # mining fee
                    balance = 0
                    balance = balance + 38
                    # mine the block
                    lastblockhash = str().zfill(32)
                    hashHandler = hashlib.sha256()
                    nonce = 0

                    while True:
                        block_header = str(nonce) + lastblockhash + abcd1.__str__()
                        hashHandler.update(block_header.encode("utf-8"))
                        hashValue = hashHandler.hexdigest()

                        nounceFound = True
                        for i in range(4):
                            if hashValue[i] != '0':
                                nounceFound = False
                        if nounceFound:
                            print('nonce:{0}, hash:{1}'.format(nonce, hashValue))
                            break
                        else:
                            nonce = nonce + 1

                    header = "{:08x}".format(nonce) + lastblockhash + abcd1.__str__()
                    body = f_content1 + f_content2 + f_content3 + f_content4
                    block = header + body

                    with open('Blockchain', 'a+') as g:
                        g.writelines(block + "\n")

                    # send tx to clientreceive for confirmation
                    for transm in f_content:
                        serverSocketF2.sendto(transm.encode(), (serverName, serverPort2))

                    # sending block to full node f1
                    serverSocketF2.sendto(block.encode(), (serverName, serverPort1))
                    print("block: " + block)