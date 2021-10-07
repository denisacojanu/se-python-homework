"""
    Ex. 8: Modificati urmatoarea bucata de cod astfel incat
    la rulare, daca valoarea care vine de la tastatura nu este 'cmi'
    sa afisam 'NOT OK'
"""

# In x vom salvea valoarea care vine de la tastatura
x = input()

# Daca valorea care vine de la tastatura este 'cmi', vom afisa 'OK'
if x == 'cmi':   # am inlocuit "da" cu "cmi"
    print('OK')
else:              # daca valoarea introdusa este alta fata de 'cmi', afisam 'NOT OK'
    print('NOT OK')
