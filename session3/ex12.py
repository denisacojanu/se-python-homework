"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""


def my_dec(func):
    def wrapper(x):
        func(x)
        with open("output12.data", "w") as file:
            file.write(x)

    return wrapper


@my_dec
def f(x):
    print(x)


user_input = input("Give me the f(x) output: ")
f(user_input)
