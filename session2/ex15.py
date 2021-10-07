"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

x = input()
x = x.lower()
vocale = ['a', 'e', 'i', 'o', 'u']

nr_vocale = 0
for i in x:
    if i in vocale:
        nr_vocale += 1
print("Numarul de vocale: ", nr_vocale)
