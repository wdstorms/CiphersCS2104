import Cipher
c1 = Cipher.KeyCipher()
enc = 'sxbaperxaleghlveewfr'
key = 'apple'
ranKey = c1.decrypt(enc, key)
print()
c2 = Cipher.CeaserCipher()
c2.decrypt(ranKey)
