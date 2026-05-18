class Pila:
    def __init__(self):
        self.__datos = []

    def push(self, elemento):
        self.__datos.append(elemento)

    def pop(self):
        if self.isEmpty():
            raise Exception("Pila vacía")
        return self.__datos.pop()

    def top(self):
        if self.isEmpty():
            raise Exception("Pila vacía")
        return self.__datos[-1]

    def isEmpty(self):
        return len(self.__datos) == 0

    def size(self):
        return len(self.__datos)



def crear_pila_mcu():
    pila = Pila()
    personajes = [
        ("Thor",             9),
        ("Hulk",             9),
        ("Hawkeye",          7),
        ("Black Widow",      8),
        ("Doctor Strange",   5),
        ("Wanda Maximoff",   7),
        ("Groot",            6),
        ("Nebula",           6),
        ("Drax",             5),
        ("Gamora",           6),
        ("Captain America", 11),
        ("Rocket Raccoon",   7),
        ("Iron Man",        11),
        ("Spider-Man",       6),
        ("Captain Marvel",   4),
        ("Nick Fury",        8),
        ("Ant-Man",          5),
        ("Falcon",           6),
        ("War Machine",      8),
        ("Loki",             8),
    ]
    for personaje in personajes:
        pila.push(personaje)
    return pila


def pila_a_lista(pila):
    """Desapila todo en una lista (índice 0 = cima) y reconstruye la pila."""
    aux = []
    while not pila.isEmpty():
        aux.append(pila.pop())          


    for elemento in reversed(aux):
        pila.push(elemento)

    return aux                         


def ejercicio_a(pila):
    print("=" * 55)
    print("a. Posición de Rocket Raccoon y Groot")
    print("=" * 55)

    lista = pila_a_lista(pila)
    buscados = {"Rocket Raccoon", "Groot"}
    encontrados = {}

    for i, (nombre, _) in enumerate(lista):
        if nombre in buscados:
            encontrados[nombre] = i + 1 

    for nombre in buscados:
        if nombre in encontrados:
            print(f"  {nombre}: posición {encontrados[nombre]}")
        else:
            print(f"  {nombre}: no encontrado en la pila")
    print()


def ejercicio_b(pila):
    print("=" * 55)
    print("b. Personajes con más de 5 películas")
    print("=" * 55)

    lista = pila_a_lista(pila)
    resultado = [(nombre, peliculas) for nombre, peliculas in lista if peliculas > 5]

    if resultado:
        for nombre, peliculas in resultado:
            print(f"  {nombre}: {peliculas} películas")
    else:
        print("  Ninguno supera las 5 películas.")
    print()


def ejercicio_c(pila):
    print("=" * 55)
    print("c. Películas de Black Widow (Viuda Negra)")
    print("=" * 55)

    lista = pila_a_lista(pila)
    for nombre, peliculas in lista:
        if nombre.lower() == "black widow":
            print(f"  Black Widow participó en {peliculas} película(s).")
            print()
            return

    print("  Black Widow no se encuentra en la pila.")
    print()


def ejercicio_d(pila):
    print("=" * 55)
    print("d. Personajes cuyo nombre empieza con C, D o G")
    print("=" * 55)

    lista = pila_a_lista(pila)
    letras = {"C", "D", "G"}
    resultado = [nombre for nombre, _ in lista if nombre[0].upper() in letras]

    if resultado:
        for nombre in resultado:
            print(f"  {nombre}")
    else:
        print("  No hay personajes con esas iniciales.")
    print()



if __name__ == "__main__":
    pila_mcu = crear_pila_mcu()

    print("\n  Pila creada con", pila_mcu.size(), "personajes MCU")
    print("  (cima → Iron Man  |  fondo → Thor)\n")

    ejercicio_a(pila_mcu)
    ejercicio_b(pila_mcu)
    ejercicio_c(pila_mcu)
    ejercicio_d(pila_mcu)