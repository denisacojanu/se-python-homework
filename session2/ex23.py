"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti daca acel string este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: stringul se citeste la fel de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 'center'
        Veti printa: False

        Veti primi: 'cojoc'
        Veti printa: True
"""

# # Rezolvare 1
x = input()
# In y stocam valoarea introdusa de la tastatura inversata
y = x[::-1]
if x == y:
    print(True)
else:
    print(False)

# Rezolvare 2
z = input()
flag = False
for i in range(0, int(len(z)/2)):
    if z[i] == z[len(z)-i-1]:
        flag = True
print(flag)

# Rezolvare 3
a = input()
rev = ''.join(reversed(a))
if a == rev:
    print(True)
else:
    print(False)
