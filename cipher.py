abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
enc = 'lfdphlvdzlfrqtxhuhg'
enc = enc.lower()
for i in range(26):
    for char in enc:
        index = abc.index(char)
        newIndex = index + i
        newIndex = newIndex % 26
        print(abc[newIndex], end='')
    print()
