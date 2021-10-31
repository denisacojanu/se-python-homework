"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""


# Method one
def my_dec(func):
    """Function that decorates f()"""

    def upper():
        result = func()
        print(f"Result before f() was decorated: {result}")
        return str(result).upper()

    return upper


# Method two
def my_dec2(func):
    """Function that decorates f()"""

    def shift_alphabetically():
        result = func()
        print(f"Result before f() was decorated: {result}")
        return "".join(chr(ord(letter) + 1) for letter in result)

    return shift_alphabetically


@my_dec
@my_dec2
def f():
    return "cmi"


print(f"Result after f() was decorated: {f()}")
