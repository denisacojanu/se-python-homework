"""
    Veti primi numere intregi de la tastatura pana primiti stringul 'exit'.
    Va trebui sa introduceti toate elemente intr-o lista si s-o afisati, dupa
    care va trebui sa creati un set (vezi ce e un set) din lista respectiva
    si sa il printati si pe acela.

    exemplu:
        Veti primi: 1, 3, 4, 5, 5, 'exit'
        Veti printa prima data: [1, 3, 4, 5, 5]
        Veti prina a doua oara: {1, 3, 4, 5}
"""
# Rezolvare
x = input("Enter a number: ")
l1 = []
while x != "exit":
    if x.isdigit():  # Verifica daca valoarea lui x contine doar cifre
        l1.append(int(x))
    else:
        print("Numarul introdus nu este un numar intreg si nu se poate adauga la lista")
    x = input("Enter a number: ")
print(l1)

s1 = {}
s1 = set(l1)
print(s1)
