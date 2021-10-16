"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""
# Rezolvare
x = int(input("Introduceti un numar: "))
suma = 0

for i in range(1, x+1): # 0 este considerat element neutru in adunare si de aceea am pornit de la 1
    suma = suma + i
print(f"Suma numerelor este: {suma}")
