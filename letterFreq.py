abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
enc = 'sxbaperxaleghlveewfr'
enc = enc.lower()
abcCount = []
for letter in abc:
    abcCount += [[letter, 0]]

for char in enc:
    index = abc.index(char)
    abcCount[index][1] += 1

print(abcCount)
    
