import hashlib

lastblockhash = '{:32x}'.format(0)
with open('E:\Bitcoin-Project\src\F1\Temp_T', 'r') as r:
    f_content1 = r.readline()
    print(f_content1)
    f_content2 = r.readline()
    print(f_content2)
    f_content3 = r.readline()
    print(f_content3)
    f_content4 = r.readline()
    print(f_content4)


def hash(mes):
    m = hashlib.sha256()
    m.update(mes.encode("utf-8"))
    m.hexdigest()
    return m


a = hash(mes=f_content1)
print(a)
b = hash(mes=f_content2)
print(b)
c = hash(mes=f_content3)
print(c)
d = hash(mes=f_content4)
print(d)

