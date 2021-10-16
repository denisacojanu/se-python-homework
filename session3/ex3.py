"""
    Ex. 3: Completati functia de mai jos, in asa fel incat sa intoarca
    o lista cu elementele pana la X (X fiind un parametru al functiei).

    Observatii:
        - X este un numar intreg (intotdeauna)
        - nu aveti voie sa folositi range()

    Rezultatul trebuie sa arate asa:
        - pentru x = 3 --> [0, 1, 2]
"""
# Rezolvare
n = int(input("Introduceti un numar: "))


def func(x):
    i = 0
    l1 = []
    while i < x:
        l1.append(i)
        i = i + 1
    return l1


l2 = func(n)
print(f"Lista cu elementele pana la {n} este: {l2}")


