"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""

# Rezolvare
x = input()

l1 = []  # am creeat o lista goala
paranteze = {")": "(", "]": "[", "}": "{"}  # stocam fiecare paranteza inchisa ca avand valoarea parantezei deschise

count = 0
for c in x:
    if c in paranteze:
        if l1 and l1[-1] == paranteze[c]:
            l1.pop()
        else:
            break
    else:
        l1.append(c)
    count = count + 1

if not l1 and count != 0:
    print(True)
else:
    print(False)
