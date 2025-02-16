"""
    Ex. 2: Modificati urmatoarea bucata de cod astfel incat
    la rulare, rezultatul afisarii sa fie cele 2 liste concatenate.
    HINT: Exista mai multe moduri prin care puteti face asta.
"""
# Ii dam variabilei l1 ca si valoare o lista cu 4 elemente (1,2,3,4)
# si variabilei l2 ca valoare o lista cu 4 elemente (5,6,7)
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7]

# Afisam listele l1 si l2 separat.
# Pentru a vedea rezultatul, rulati acest script.
print(l1)
print(l2)

# Metoda 1
print(f"Listele concatenate: {l1 + l2}")

# Metoda 2
l1.extend(l2)
print(f"Listele concatenate: {l1}")
