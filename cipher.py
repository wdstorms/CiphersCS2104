class CeaserCipher:

    def __init__(self):
        self.abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def decrypt(self, enc):
        self.enc = enc.lower()
        for i in range(26):
            for char in enc:
                index = self.abc.index(char)
                newIndex = index + i
                newIndex = newIndex % 26
                print(self.abc[newIndex], end='')
            print()

class KeyCipher:
    
    def __init__(self):
        self.abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        

    # decrypts a string based on a key string
    def decrypt(self, encrypted, key):
        enc = encrypted.lower()
        key = key.lower()
        keyLength = len(key)
        k = 0
        out = ''
        for char in enc:
            index = self.abc.index(char)
            deltaChar = key[k]
            delta = self.abc.index(deltaChar)
            newIndex = index + delta
            newIndex = newIndex % 26
            out += self.abc[newIndex]
            k = (k + 1) % keyLength

        print(out)
        return out
