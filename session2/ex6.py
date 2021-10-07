"""
    Ex. 6: Modificati urmatoarea bucata de cod astfel incat
    la rulare, la a doua afisare, sa avem inca un element in dictionar,
    cu cheia 3 si valoarea 'CMI3'
"""
import pprint
# In variabila d1 vom salva urmatorul dictionar:
d1 = {
    1: 'CMI',
    2: 'CMI2'
}

# Afisam dictionarul inainte de schimbare
print(d1)

# Schimbam valoarea de la cheia 2, din 'CMI2' in 'CMI'
d1[2] = 'CMI'

# Metoda 1:  Am adaugat in dictionar inca un element cu cheia 3 si valoarea 'CMI3'
d1[3] = 'CMI3'

# Afisam dictionarul dupa schimbare
print("Metoda 1: ", d1)

# Metoda 2
d1.update({3: 'CMI3'})
print("Metoda 2: ", d1)
