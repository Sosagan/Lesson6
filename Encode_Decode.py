def enc(t):
    bytes = []
    for i in t:
        a = i.encode('utf-8')
        bytes.append(a)
    return bytes
a = input().split()
def dec(d):
    b = []
    for i in d:
        word = bytes.decode(i, 'utf-8')
        b.append(word)
    return b
enc_a = enc(a)
print(enc_a)
print(dec(enc_a))


