"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""

# Rezolvare metoda 1
x = input("Introduceti un cuvant: ")
vocale = ['a', 'e', 'i', 'o', 'u']

nr_vocale = 0
nr_consoane = 0

x = x.replace(' ', '')  # Am adaugat replace deoarece daca introducem 2 cuvinte, spatiul era vazut ca o consoana
for i in x:
    if i in vocale:
        nr_vocale += 1
    elif i not in vocale and i != ' ':
        nr_consoane += 1
print("Numarul de vocale este: ", nr_vocale)
print("Numarul de consoane este: ", nr_consoane)

# Rezolvare metoda 2
x = input("Introduceti un cuvant: ")
vocale = ['a', 'e', 'i', 'o', 'u']

nr_vocale = 0
nr_consoane = 0

x = x.replace(' ', '')  # Am adaugat replace deoarece daca introducem 2 cuvinte, spatiul era vazut ca o consoana
for i in x:
    if i in vocale:
        nr_vocale += 1
    else:
        nr_consoane += 1
print("Numarul de vocale este: ", nr_vocale)
print("Numarul de consoane este: ", nr_consoane)
