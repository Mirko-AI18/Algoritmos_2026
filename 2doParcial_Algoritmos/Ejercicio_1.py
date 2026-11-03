from tree import BinaryTree
from pokemons import DATOS

# A) Clase Pokemon y carga de datos

class Pokemon:
    def __init__(self, numero, nombre, tipos, debilidades, mega, gigamax):
        self.__numero = numero
        self.__nombre = nombre
        self.__tipos = tipos
        self.__debilidades = debilidades
        self.__mega = mega
        self.__gigamax = gigamax

    def get_numero(self):
        return self.__numero

    def get_nombre(self):
        return self.__nombre

    def get_tipos(self):
        return self.__tipos

    def get_debilidades(self):
        return self.__debilidades

    def get_mega(self):
        return self.__mega

    def get_gigamax(self):
        return self.__gigamax

    def set_numero(self, numero):
        self.__numero = numero

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_tipos(self, tipos):
        self.__tipos = tipos

    def set_debilidades(self, debilidades):
        self.__debilidades = debilidades

    def set_mega(self, mega):
        self.__mega = mega

    def set_gigamax(self, gigamax):
        self.__gigamax = gigamax

    def __str__(self):
        return (f"N°: {self.__numero} | Nombre: {self.__nombre} | Tipos: {self.__tipos} | "
                f"Debilidades: {self.__debilidades} | Mega: {self.__mega} | Gigamax: {self.__gigamax}")


# Arboles por nombre, numero y tipo
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for dato in DATOS:
    pokemon = Pokemon(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
    arbol_nombre.insert_node(pokemon.get_nombre(), pokemon)
    arbol_numero.insert_node(pokemon.get_numero(), pokemon)
    for tipo in pokemon.get_tipos():
        nodo = arbol_tipo.search(tipo)
        if nodo is None:
            arbol_tipo.insert_node(tipo, [pokemon])
        else:
            nodo.other_values.append(pokemon)


# B) Mostrar los datos a partir del numero y del nombre (por proximidad)

def buscar_por_numero(arbol: BinaryTree, numero: int):
    nodo = arbol.search(numero)
    if nodo is not None:
        print(nodo.other_values)
    else:
        print("No se encontro el pokemon")


def buscar_por_proximidad(arbol: BinaryTree, texto: str):
    texto = texto.lower()

    def __buscar(root):
        if root is not None:
            __buscar(root.left)
            if texto in root.value.lower():
                print(root.other_values)
            __buscar(root.right)

    __buscar(arbol.root)


print("B) Busqueda por numero (25)")
buscar_por_numero(arbol_numero, 25)
print()
print("B) Busqueda por proximidad ('bul')")
buscar_por_proximidad(arbol_nombre, "bul")
print()

# C) Nombres de los Pokemons de un determinado tipo

def mostrar_nombres_por_tipo(arbol: BinaryTree, tipo: str):
    nodo = arbol.search(tipo)
    print(f"Pokemons de tipo {tipo}:")
    if nodo is not None:
        for pokemon in nodo.other_values:
            print(pokemon.get_nombre())
    print()


for tipo in ["Fantasma", "Fuego", "Acero", "Eléctrico"]:
    mostrar_nombres_por_tipo(arbol_tipo, tipo)

# D) Listados ascendentes por numero y por nombre, y listado por nivel por nombre

def inorden_pokemon(arbol: BinaryTree):

    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            print(root.other_values.get_numero(), "-", root.other_values.get_nombre())
            __inorden(root.right)

    __inorden(arbol.root)


print("D) Listado ascendente por numero")
inorden_pokemon(arbol_numero)
print()
print("D) Listado ascendente por nombre")
inorden_pokemon(arbol_nombre)
print()
print("D) Listado por nivel por nombre")
arbol_nombre.by_level()
print()

# E) Pokemons debiles frente a Jolteon, Lycanroc o Tyrantrum (por lo menos uno de los tres)

def debiles_frente_a(arbol_n: BinaryTree, arbol_num: BinaryTree, nombres: list):
    tipos = []
    for nombre in nombres:
        nodo = arbol_n.search(nombre)
        if nodo is not None:
            for tipo in nodo.other_values.get_tipos():
                if tipo not in tipos:
                    tipos.append(tipo)

    print(f"Pokemons debiles frente a {nombres} (tipos: {tipos}):")

    def __recorrer(root):
        if root is not None:
            __recorrer(root.left)
            debilidades = root.other_values.get_debilidades()
            for tipo in tipos:
                if tipo in debilidades:
                    print(root.other_values.get_nombre())
                    break
            __recorrer(root.right)

    __recorrer(arbol_num.root)
    print()


debiles_frente_a(arbol_nombre, arbol_numero, ["Jolteon", "Lycanroc", "Tyrantrum"])

# F) Todos los tipos y cuantos Pokemons hay de cada tipo

def mostrar_cantidad_por_tipo(arbol: BinaryTree):

    def __inorden(root):
        if root is not None:
            __inorden(root.left)
            print(f"{root.value}: {len(root.other_values)}")
            __inorden(root.right)

    __inorden(arbol.root)


print("F) Cantidad de Pokemons por tipo")
mostrar_cantidad_por_tipo(arbol_tipo)
print()

# G) y H) Cantidad de Pokemons con megaevolucion y con gigamax

def contar_mega_gigamax(arbol: BinaryTree):

    def __contar(root):
        if root is None:
            return 0, 0
        mega_izq, giga_izq = __contar(root.left)
        mega_der, giga_der = __contar(root.right)
        mega = mega_izq + mega_der
        giga = giga_izq + giga_der
        if root.other_values.get_mega():
            mega += 1
        if root.other_values.get_gigamax():
            giga += 1
        return mega, giga

    return __contar(arbol.root)


cant_mega, cant_gigamax = contar_mega_gigamax(arbol_numero)
print(f"G) Pokemons con megaevolucion: {cant_mega}")
print(f"H) Pokemons con forma gigamax: {cant_gigamax}")
