class CaesarCipher:

    def __init__(self):
        self.abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    def decrypt26(self, enc):
        enc = enc.lower()
        out = []
        for i in range(26):
            dec = self.decrypt(enc, i)
            out += [dec]
        return out

    def decrypt(self, enc, rotation):
        enc = enc.lower()
        unrot = (26 - rotation) % 26
        dec = ''
        for char in enc:
            if (char == ' '):
                print(' ', end='')
                dec += ' '
            else:
                index = self.abc.index(char)
                newIndex = index + unrot
                newIndex = newIndex % 26
                print(self.abc[newIndex], end='')
                dec += self.abc[newIndex]
        print()
        return dec

class KeyCipher:
    
    def __init__(self):
        self.abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        

    # decrypts a string based on a key string
    def decrypt(self, encrypted, key):
        enc = encrypted.lower()
        key = key.lower()
        keyLength = len(key)
        k = 0
        out = ''
        for char in enc:
            if (char == ' '):
                    out+=' '
            else:
                index = self.abc.index(char)
                deltaChar = key[k]
                delta = self.abc.index(deltaChar)
                newIndex = index + delta
                newIndex = newIndex % 26
                out += self.abc[newIndex]
                k = (k + 1) % keyLength

        print(out)
        return out

class Atbash:

    def __init__(self):
        self.abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        self.zyx = []
        for i in range(26):
            self.zyx += self.abc[25-i]
            
    def decrypt(self, s):
        out = ''
        for char in s.lower():
            index = self.abc.index(char)
            out += self.zyx[index]
        return out

class Base64:

    def __init__(self):
        self.abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

class LetterFreq:

    def __init__(self):
        self.abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        self.freq = []
        
    def setFreq(self, s):
        s = s.lower()
        newFreq = []
        for letter in self.abc:
            newFreq += [[letter, 0]]

        for char in s:
            if (char != ' '):
                index = self.abc.index(char)
                newFreq[index][1] += 1

        self.freq = newFreq
        return self.freq

    def getFreq(self):
        return self.freq

    def __str__(self):
        out = ''
        for pair in self.freq:
            out += (pair[0] + ": " + str(pair[1]) + '\n')
        return out


class Reverse:

    def __init__(self):
        a = 1

    def reverse(self, s):
        out = ""
        for char in s:
            out = char + out

        return out

    
            











        
