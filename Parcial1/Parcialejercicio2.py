from typing import List
from collections import deque
from super_heroes_data import superheroes


# Ejercicio 2: Dada una lista de personajes de marvel (usar el archivo adjunto) debe tener 100 o mas, resolver:
# Listado ordenado de manera ascendente por nombre de los personajes.
# Determinar en que posicion esta The Thing y Rocket Raccoon.
# Listar todos los villanos de la lista.
# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# Listar los superheores que comienzan con Bl, G, My, y W.
# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# Listado de superheroes ordenados por fecha de aparacion.
# Modificar el nombre real de Ant Man a Scott Lang.
# Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# Eliminar a Electro y Baron Zemo de la lista y mostrar su informacion si estaba en la lista.

heroes: List = list(superheroes)


def obtener_nombre(heroe):
    return heroe["name"]

def obtener_nombre_real(heroe):
    if heroe["real_name"] is None:
        return ""
    return heroe["real_name"]

def obtener_fecha(heroe):
    return heroe["first_appearance"]


print("1. Ordenados por nombre")
por_nombre = sorted(heroes, key=obtener_nombre)
for heroe in por_nombre:
    print(heroe["name"])

print("2. Posicion de The Thing y Rocket Raccoon")
for objetivo in ["The Thing", "Rocket Raccoon"]:
    for i in range(len(por_nombre)):
        if por_nombre[i]["name"] == objetivo:
            print(objetivo, "esta en la posicion", i + 1)

print("3. Villanos")
for heroe in heroes:
    if heroe["is_villain"] == True:
        print(heroe["name"])

print("4. Cola de villanos antes de 1980")
cola_villanos = deque()
for heroe in heroes:
    if heroe["is_villain"] == True and heroe["first_appearance"] < 1980:
        cola_villanos.append(heroe)
for villano in cola_villanos:
    print(villano["name"], villano["first_appearance"])

print("5. Heroes que empiezan con Bl, G, My, W")
for heroe in heroes:
    nombre = heroe["name"]
    if nombre.startswith("Bl") or nombre.startswith("G") or nombre.startswith("My") or nombre.startswith("W"):
        print(nombre)

print("6. Ordenados por nombre real")
por_nombre_real = sorted(heroes, key=obtener_nombre_real)
for heroe in por_nombre_real:
    print(heroe["real_name"], "-", heroe["name"])

print("7. Ordenados por fecha de aparicion")
por_fecha = sorted(heroes, key=obtener_fecha)
for heroe in por_fecha:
    print(heroe["first_appearance"], heroe["name"])

print("8. Cambiar nombre real de Ant Man")
for heroe in heroes:
    if heroe["name"] == "Ant Man":
        print("Nombre anterior:", heroe["real_name"])
        heroe["real_name"] = "Scott Lang"
        print("Nombre nuevo:", heroe["real_name"])

print("9. Personajes con time-traveling o suit en su bio")
for heroe in heroes:
    if "time-traveling" in heroe["short_bio"] or "suit" in heroe["short_bio"]:
        print(heroe["name"])

print("10. Eliminar Electro y Baron Zemo")
a_eliminar = ["Electro", "Baron Zemo"]
for nombre in a_eliminar:
    encontrado = None
    for heroe in heroes:
        if heroe["name"] == nombre:
            encontrado = heroe
    if encontrado != None:
        heroes.remove(encontrado)
        print(encontrado["name"], "eliminado")
        print("Nombre real:", encontrado["real_name"])
        print("Alias:", encontrado["alias"])
        print("Primera aparicion:", encontrado["first_appearance"])
        print("Es villano:", encontrado["is_villain"])
    else:
        print(nombre, "no estaba en la lista")

print("Total de personajes:", len(heroes))