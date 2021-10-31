"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""
# Rezolvare metodata 1 cu liste
x = input()
# declaram o lista goala
l1 = []
# caracterele din x le punem in lista l1
l1[:0] = x
l2 = []
for i in range(len(l1)):
    if i % 2 == 0:
        l2.append(l1[i].upper())
    else:
        l2.append(l1[i].lower())

"""
    In x punem elementele din lista l2 care contine 
    caracterele de pe pozitiile pare cu litere mari
"""
x = "".join(map(str, l2))
print(x)

# Rezolvare metoda 2 fara liste
x = input()
y = ""
for i in range(len(x)):
    if i % 2 == 0:
        y = y + x[i].upper()
    else:
        y = y + x[i].lower()
print(y)
