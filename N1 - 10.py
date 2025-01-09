frase = str(input('Digite uma frase: ')).split()

for c1 in range(0,len(frase)):
    for p in frase:
        for c2 in range(0, len(frase)):
            if c1 != c2:
                for i in frase:
                    if p == i:
                        frase.pop(c2)
                        frase.insert(c1, p)

print(frase)