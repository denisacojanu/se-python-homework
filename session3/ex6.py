"""
    Ex. 6: Scrieti o functie cu un singur parametru (string) care
    intoarce un string cu toate literele stringului primit +1 (adica urmatoarea
    litera din alfabet)

    Raspuns:
        - func('aabbcc')
            ---> 'bbccdd'
"""


def increase_letters_alphabetically_by_one(my_string):
    """
        The generator iterates over each letter in the string value and increments it by one using
         the chr(ord(letter)+1) methodology. It then uses ''.join() to
         convert the letters in the generator back into a string.
         The ord() method in Python converts a character into its Unicode code value
    """
    return "".join(chr(ord(letter) + 1) for letter in my_string)


input_string = input("Give me a string: ")
print(f"The new string is: {increase_letters_alphabetically_by_one(input_string)}")
