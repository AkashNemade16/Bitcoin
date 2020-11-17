from socket import *
import hashlib

turn = 1
initial_balance = 0
initial_balance_hex = hex(initial_balance)

serverPort2 = 11000  # F2
serverPort1 = 20000  # client-recieve
serverPort = 10000  # F1
serverSocketF1 = socket(AF_INET, SOCK_DGRAM)
serverName = 'localhost'
serverSocketF1.bind(('', serverPort))
print('The server is ready to receive')

while 1:
    message, clientAddress = serverSocketF1.recvfrom(2048)
    client_send = clientAddress
    modifiedMessage = message.decode()
    print(modifiedMessage)
    clientA = modifiedMessage
    # serverSocket.sendto(clientA.encode(), (serverName, serverPort1))
    serverSocketF1.sendto(clientA.encode(), (serverName, serverPort2))

    message1, clientAddress1 = serverSocketF1.recvfrom(2048)
    f1 = clientAddress1
    msg = message1.decode()
    print(msg)

    if client_send == clientAddress:  # receive tx and appending to temp_t.txt
        with open('Temp_T', '+a') as w:
            w.write(clientA.lstrip() + "\n")
        #
        with open('Temp_T', 'r') as f:
            counter = 0
            f_content = f.read()
            coList = f_content.split("\n")
            for i in coList:
                if i:
                    counter += 1
            # print(counter)
        if counter == 3:
            turn += 1
            if (turn % 2) == 1:
                serverSocketF1.close()
            else:
                lastblockhash = str().zfill(32)
                # if counter == 4:
                with open('Temp_T', 'r') as r:
                    f_content1 = r.readline()
                    print(f_content1)
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

                block = block_header + f_content1 + f_content2 + f_content3 + f_content4
                print(block)
                file = open("Temp_T", "r+")
                file.truncate(0)
                file.close()

        # if f1 == clientAddress1:
