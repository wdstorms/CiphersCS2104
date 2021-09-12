import Cipher
c1 = Cipher.KeyCipher()
c2 = Cipher.CaesarCipher()
c3 = Cipher.Atbash()
c4 = Cipher.Base64()
f1 = Cipher.LetterFreq()
enc = 'BGDTCU BCEJ BCXKGT CPF BCPG BQQOGF VJTQWIJ VJG BQQ'
f1.setFreq(enc)
print(f1)
c2.decrypt26(enc)


input('\nenter to esc')
