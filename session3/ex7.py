"""
    Ex. 7: Scrieti o functie care sa primeasca trei parametri
        - prefix (string)
        - word (string)
        - suffix (string)
    Si trebuie sa intoarca cuvantul cu prefixul si sufixul adaugate.

    Raspuns:
        - pentru prefix = 'a', suffix = 'b' si word = 'x'
            ---> 'axb'

    Observatii:
        - functia trebuie sa aiba MAXIM 1 linie de cod ca si body
"""


def final_word(prx, wrd, sfx):
    """The function returns a concatenated string"""
    return prx + wrd + sfx


prefix = input("Give me a prefix: ")
word = input("Give me a word: ")
suffix = input("Give me a suffix: ")
print(f"Final word is: {final_word(prefix, word, suffix)}")
