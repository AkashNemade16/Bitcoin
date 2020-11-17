# import hashlib
#
#
#
# # var1 = hex(var)
# # var2 = int(var1, 16)
# # var3 = hex(var2)
# # print(var3)
#
# lastblockhash = str().zfill(32)
# print(lastblockhash)
# with open('E:\Bitcoin-Project\src\F1\Temp_T', 'r') as r:
#     f_content1 = r.readline()
#     print(f_content1)
#     f_content2 = r.readline()
#     print(f_content2)
#     f_content3 = r.readline()
#     print(f_content3)
#     f_content4 = r.readline()
#     print(f_content4)
#
#
# def hash(mes):
#     m = hashlib.sha256()
#     m.update(mes.encode("utf-8"))
#     m.hexdigest()
#     return m
#
#
# a = hash(mes=f_content1)
# # print(a)
# b = hash(mes=f_content2)
# # print(b)
# c = hash(mes=f_content3)
# # print(c)
# d = hash(mes=f_content4)
# # print(d)
#
# ab = a.__str__() + b.__str__()
# ab1 = hash(ab)
# print(ab1)
#
# cd = str(c) + str(d)
# cd1 = hash(cd)
# print(cd1)
# #
# abcd = str(ab1) + str(cd1)
# abcd1 = hash(abcd)
# print(abcd1)
#
# hashHandler = hashlib.sha256()
# nonce = 0
#
# while True:
#     block_header = str(nonce) + lastblockhash + abcd1.__str__()
#     hashHandler.update(block_header.encode("utf-8"))
#     hashValue = hashHandler.hexdigest()
#
#     nounceFound = True
#     for i in range(4):
#         if hashValue[i] != '0':
#             nounceFound = False
#     if nounceFound:
#         print('nonce:{0}, hash:{1}'.format(nonce, hashValue))
#         break
#     else:
#         nonce = nonce + 1
# with open('E:\Bitcoin-Project\src\F1\Temp_T', 'r+') as k:
#     toremove = k.readlines()
# # with open('Temp_T', 'a+') as l:
# #     for lines in toremove:
# #         l.write(lines.strip())
file = open("Temp_T", "r+")
file.truncate(0)
file.close()