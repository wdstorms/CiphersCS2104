import Cipher

d = Cipher.KeyCipher()

enc = "sxbaperxaleghlveewfr"

key = "apple"
dec = d.decrypt(enc, key)

c = Cipher.CaesarCipher()


print(c.decrypt(dec))
