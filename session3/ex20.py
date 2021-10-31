"""
    Ex. 20: Deschideti fisierul .json creat la exercitiul anterior, cititi
    continutul si returnati un dictionar (dictionarul de acolo).

    Toate astea le veti face intr-o functie read_from_file(file), unde
    file este numele fisierului primit dat ca parametru.
"""
import json


def read_from_file(file):
    with open(file, "r") as json_file:
        data = json.load(json_file)
    return data


print(f"Result from json file: {read_from_file('test.json')}")
