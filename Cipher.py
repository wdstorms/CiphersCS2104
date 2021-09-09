class CaesarCipher:

    def __init__(self):
        self.abc = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

    def decrypt(self, enc):
        enc = enc.lower()
        out = []
        for i in range(26):
            dec = ''
            for char in enc:
                if (char == ' '):
                    print(' ', end='')
                    dec += ' '
                else:
                    index = self.abc.index(char)
                    newIndex = index + i
                    newIndex = newIndex % 26
                    print(self.abc[newIndex], end='')
                    dec += self.abc[newIndex]
            out += [dec]
            print()
        return out

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
        freq = []
        for letter in self.abc:
            freq += [[letter, 0]]

        for char in s:
            index = self.abc.index(char)
            freq[index][1] += 1

        self.freq = freq
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

    
            











        
