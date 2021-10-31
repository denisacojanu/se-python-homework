"""
    Ex. 11: Scrieti un decorator care sa logheze outputul unei functii
    pe care o decoreaza, intr-un fisier "output11.data".

    https://www.w3schools.com/python/python_file_write.asp

    Functia decorata este f.
"""


def my_dec(func):
    def wrapper():
        result = func()
        with open("output11.data", "w") as file:
            file.write(result)

    return wrapper


@my_dec
def f():
    return "CMI"


f()
