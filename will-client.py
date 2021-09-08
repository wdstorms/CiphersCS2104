import Cipher

r = Cipher.Reverse()

enc = "my racecar"

dec = r.reverse(enc)

print(dec)
