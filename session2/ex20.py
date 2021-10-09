"""
    Veti primi un string de la tastatura.
    Veti primi un numar intreg de la tastatura, x.
    Va trebui sa creati un dictionar care sa contina ca si chei, toate numerele
    pana la x, iar ca si valori caracterele de pe indexurile corespunzatoare.

    Observatii:
        - lungimea stringului va fi mereu egala cu numarul primit
        - indexarea in python incepe de la 0 (prima cheie va fi 0)

    exemplu:
        Veti primi: 'cmi', 3
        Veti printa: {
            0: 'c',
            1: 'm',
            2: 'i'
        }
"""
# Rezolvare

from pprint import pprint
a = input()
x = input()
x = int(x)

while x != len(a):
    print("Numarul introdus este mai mare decat lungimea stringului. ")
    print("Introduceti alt numar: ")
    x = int(input())

l1 = []
l2 = []

for i in range(x):
    l1.append(i)

for i in a:
    l2.append(i)

d1 = dict(zip(l1, l2))
pprint(d1, width=2)

