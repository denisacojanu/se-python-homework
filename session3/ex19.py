"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""
import json
import random
from string import ascii_letters


def create_json_file(my_string):
    l1 = []
    l2 = []
    l1 = list(random.sample(range(0, 10), 4))

    for a in range(4):
        l2.append("".join(random.choices(ascii_letters, k=random.randint(3, 6))))

    d1 = dict(zip(l1, l2))

    with open(my_string + ".json", "w") as file:
        json.dump(d1, file, indent=4)


user_input = input("Give me a string: ")
create_json_file(user_input)
