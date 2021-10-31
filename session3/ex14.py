"""
    Ex. 14: Creati o functie get_me_numbers, care sa aiba o functie interioara
    multiply_by_5.

    multiply_by_5 primeste un parametru x, si il inmulteste cu 5, si intoarce
    rezultatul.

    get_me_numbers, primeste un parametru x, adauga 5 si apoi se foloseste
    de multiply_by_5 pentru a il inmulti cu 5, iar la final, mai adauga 3.

    Exemplu:
        daca apelez get_me_numbers(3)
            --> (3 + 5) * 5 + 3 = 43
"""


def get_me_numbers(x):
    """
        Function with internal function: multiply_by_5
        Return an number after some operations
    """

    def multiply_by_5(y):
        return y * 5

    x = x + 5
    x = multiply_by_5(x)
    x = x + 3
    return x


user_input = int(input("Give me a number: "))
print(f"Result: {get_me_numbers(user_input)}")
