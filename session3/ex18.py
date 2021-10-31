"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def sum_list(l1):
    if len(l1) == 0:
        return 0
    else:
        return l1[0] + sum_list(l1[1:])


def build_list_from_input():
    """Returns a list given as input"""
    l1 = input("Enter elements of a list separated by space: ")
    l2 = l1.split()

    # convert each item to int type
    for i in range(len(l2)):
        l2[i] = int(l2[i])

    return l2


my_list = build_list_from_input()
print(f"Sum result is: {sum_list(my_list)}")
