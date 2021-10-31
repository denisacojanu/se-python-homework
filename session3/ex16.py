"""
    Ex. 16: Scrieti o functie upper care sa intoarca un text uppercase complet,
    primind un parametru my_str (string).
    --> f('cmi') --> 'CMI'

    Scrieti o functie lower care sa intoarca un text lowercase complet,
    primind un parametru my_str (string).
    --> f('CMI') --> 'cmi'

    Veti primi un input de la tastatura, un string.

    Scrieti o alta functie call_changers, care sa primeasca o functie ca si
    parametru, iar daca inputul are un numar par de caractere, va printa inputul
    cu uppercase, altfel, va printa inputut lowercase.

    Exemplu:
        - veti primi input: 'ceva'
            ---> CEVA
        - veti primi input: 'cEVa1'
            ---> ceva1
"""


def upper_string(my_str):
    return my_str.upper()


def lower_string(my_str):
    return my_str.lower()


def call_changers(func):
    return func


user_input = input("Give me a string: ")


if len(user_input) % 2 == 0:
    print(
        f"\nInput has an even number of characters. "
        f"\nResult upper: {call_changers(upper_string(user_input))}"
    )

else:
    print(
        f"\nInput has an odd number of characters. "
        f"\nResult lower: {call_changers(lower_string(user_input))}"
    )
