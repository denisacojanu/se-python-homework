"""
    Veti primi un string de la tastatura.
    Veti primi doua numere intregi de la tastatura, x, y.
    Va trebui sa printati substringul de la indexul x la indexul y (inclusiv).

    exemplu:
        Veti primi: 'Center for Intelligent Machines', 2, 5
        Veti printa: 'nter'
"""
# Rezolvare

a = input("Introduceti stringul: ")
x, y = input("Introduceti cele 2 numere intregi: ").split()
x = int(x)
y = int(y)
print(a[x:y+1])
