"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""

# Rezolvare
# a = int(input())
# flag = False
# z = str(a)
# for i in range(0, int(len(z)/2)):
#     if z[i] == z[len(z)-i-1]:
#         flag = True
# print(flag)

# Rezolvare 2
x = int(input("Enter a number: "))
temp = x
rev = 0
while x > 0:
    digit = x % 10
    rev = rev * 10 + digit
    x = x // 10
if temp == rev:
    print(True)
else:
    print(False)
