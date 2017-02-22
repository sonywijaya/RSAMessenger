def encrypt(e, n, text):
    asciiVal = [ord(c) for c in text]
    asciiEn = []
    for i in asciiVal:
        asciiEn.append((i**e) % n)
    return asciiEn

def decrypt(d, n, textEn):
    asciiDe = []
    for i in textEn:
        asciiDe.append((i**d) % n)
    return ''.join(chr(i) for i in asciiDe)
