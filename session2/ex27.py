"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
#Rezolvare metoda 1
import random
import string

x = int(input("Enter a number: "))
result = ''.join(random.choice(string.ascii_letters) for i in range(x))
print(result)

