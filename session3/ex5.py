"""
    Ex. 5: Scrieti o functie cu un singur parametru (o lista) care sa
    adauge 1 tuturor elementelor din lista.

    Raspunsul corect:
        - func([1, 2, 3])
            ---> [2, 3, 4]

    Observatii:
        - functia trebuie sa fie MAXIM o linie de cod (2, daca luam in calcul
        si definitia functiei)
        - hint: list comprehensions (google it if you don't know it already)
"""

"""
    List comprehension offers a shorter syntax when you want to create a new list based on
    the values of an existing list.  
"""


def increase_each_element_by_one(my_list):
    """Returns a new list with each element increased by one"""
    return [x + 1 for x in my_list]


def build_list_from_input():
    """Returns a list given as input"""
    l1 = input("Enter elements of a list separated by space: ")
    l2 = l1.split()

    # convert each item to int type
    for i in range(len(l2)):
        l2[i] = int(l2[i])

    return l2


print(f"The new list is: \n{increase_each_element_by_one(build_list_from_input())}")
