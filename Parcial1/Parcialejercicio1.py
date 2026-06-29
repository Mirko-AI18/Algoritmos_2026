from typing import List

# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.

lista_15: List = [
    "Captain America",
    "Iron Man",
    "Thor",
    "Hulk",
    "Black Widow",
    "Spiderman",
    "Wolverine",
    "Storm",
    "Black Panther",
    "Vision",
    "Scarlet Witch",
    "Ant Man",
    "Wasp",
    "Doctor Strange",
    "Silver Surfer"
]


def buscar_capitan_america(lista, i=0):
    if i >= len(lista):
        return False
    if lista[i] == "Captain America":
        return True
    return buscar_capitan_america(lista, i + 1)


def listar_heroes(lista, i=0):
    if i >= len(lista):
        return
    print(lista[i])
    listar_heroes(lista, i + 1)


print("Lista de heroes")
listar_heroes(lista_15)

resultado = buscar_capitan_america(lista_15)
print("Esta Captain America en la lista:", resultado)


