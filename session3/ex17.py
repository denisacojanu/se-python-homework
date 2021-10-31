"""
    Ex. 17: Scrieti un decorator care scrie outputul unei functii intr-un fisier
    "output17.data", dar sa nu suprascrie fisierul daca scriptul e rulat de
    mai multe ori, iar contentul nou sa fie pe o noua linie.

    Scrieti o functie f care sa primeasca un intreg (x) ca parametru si sa
    genereze un string aleator din x litere.

    Decorati f cu decoratorul de mai sus.

    Exemplu:
        la prima rulare, x = 3, stringul generat = 'cmi', fisierul arata asa:
            cmi
        la a doua rulare, x = 6, stringul generat = 'cmicmi', fisierul arata:
            cmi
            cmicmi
        la a treia rulare, x = 1, stringul generat = 'b', fisierul arata asa:
            cmi
            cmicmi
            b
"""

from random import choice
from string import ascii_letters


def my_dec(func):
    def log_output_function(z):
        result = func(z)
        with open("output17.data", "a") as file:
            file.write(f"{result}\n")

    return log_output_function


@my_dec
def f(x):
    """Function returns a random string with lengh = x"""
    return "".join(choice(ascii_letters) for i in range(x))


y = int(input("Give me a number: "))
f(y)
