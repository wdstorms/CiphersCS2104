abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
enc = 'sxbaperxaleghlveewfr'
enc = enc.lower()
key = 'apple'
key = key.lower()
keyLength = len(key)
k = 0
out = ''
for char in enc:
    index = abc.index(char)
    deltaChar = key[k]
    delta = abc.index(deltaChar)
    newIndex = index + delta
    newIndex = newIndex % 26
    print(abc[newIndex], end='')
    out += abc[newIndex]
    k = (k + 1) % keyLength

print(' | ', end='')

solved = out
for char in solved:
    index = abc.index(char)
    newIndex = index + 1
    newIndex = newIndex % 26
    print(abc[newIndex], end='')

print()

input('enter to esc')
