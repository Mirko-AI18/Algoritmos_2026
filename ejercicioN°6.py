# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
# casa de comic a la que pertenece (Marvel o DC) y biografa, implementar la funciones necesa
# rias para poder realizar las siguientes actividades:
#   a. eliminar el nodo que contiene la información de Linterna Verde;
#   b. mostrar el año de aparición de Wolverine;
#   c. cambiar la casa de Dr. Strange a Marvel;
#   d. mostrar el nombre de aquellos superhéroes que en su biografa menciona la palabra
#      “traje” o “armadura”;
#   e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#      sea anterior a 1963;
#   f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#   g. mostrar toda la información de Flash y Star-Lord;
#   h. listar los superhéroes que comienzan con la letra B, M y S;
#   i. determinar cuántos superhéroes hay de cada casa de comic.

from list_ import List

class SuperHeroe():
    def __init__(self, nombre:str, anio_aparicion:int, casa:str, biografia:str):
        self.__nombre = nombre
        self.__anio_aparicion = anio_aparicion
        self.__casa = casa
        self.__biografia = biografia

    def get_nombre(self):
        return self.__nombre
    
    def get_anio_aparicion(self):
        return self.__anio_aparicion

    def get_casa(self):
        return self.__casa

    def get_biografia(self):
        return self.__biografia
    
    def set_casa(self, casa:str):
        self.__casa = casa
    
    def __str__(self):
        return f"[Nombre: {self.__nombre} | Año de aparicion: {self.__anio_aparicion} | Casa: {self.__casa} | Biografia: {self.__biografia}]"


lista_de_superheroes = List()

# Agregar superhéroes a la lista
lista_de_superheroes.append(SuperHeroe("Superman", 1938, "DC", "Alien con poderes sobrehumanos, vuela y tiene traje azul"))
lista_de_superheroes.append(SuperHeroe("Batman", 1939, "DC", "Detective con armadura de murciélago y gadgets avanzados"))
lista_de_superheroes.append(SuperHeroe("Mujer Maravilla", 1941, "DC", "Princesa guerrera amazona con traje iconic"))
lista_de_superheroes.append(SuperHeroe("Linterna Verde", 1940, "DC", "Utiliza un anillo que genera constructos de luz verde"))
lista_de_superheroes.append(SuperHeroe("Wolverine", 1974, "Marvel", "Mutante con factor de curación y garras de adamantio"))
lista_de_superheroes.append(SuperHeroe("Dr. Strange", 1963, "DC", "Maestro de las artes místicas y magia negra"))
lista_de_superheroes.append(SuperHeroe("Iron Man", 1962, "Marvel", "Millonario con armadura high-tech de metal"))
lista_de_superheroes.append(SuperHeroe("Capitana Marvel", 1968, "Marvel", "Astronauta con poderes cósmicos y fuerza sobrehumana"))
lista_de_superheroes.append(SuperHeroe("Flash", 1956, "DC", "Posee super velocidad que le permite correr a velocidad de la luz"))
lista_de_superheroes.append(SuperHeroe("Star-Lord", 1976, "Marvel", "Líder del equipo Guardianes de la Galaxia"))
lista_de_superheroes.append(SuperHeroe("Black Panther", 1966, "Marvel", "Rey de Wakanda con traje tech avanzado"))
lista_de_superheroes.append(SuperHeroe("Spider-Man", 1962, "Marvel", "Joven con poderes de araña y traje rojo"))

# Agregar criterios de busqueda

def by_name(item: SuperHeroe):
    return item.get_nombre()

lista_de_superheroes.add_criterion("nombre",by_name)

def by_year(item: SuperHeroe):
    return item.get_anio_aparicion()

lista_de_superheroes.add_criterion("anio",by_year)

#   a. eliminar el nodo que contiene la información de Linterna Verde;

def eliminar_linterna_verde(lista: List):
    lista.delete_value("Linterna Verde","nombre")

#   b. mostrar el año de aparición de Wolverine;

def obtener_anio_wolverine(lista: List[SuperHeroe]) -> int:
    ubicacion = lista.search("Wolverine", "nombre")

    return lista[ubicacion].get_anio_aparicion()


#   c. cambiar la casa de Dr. Strange a Marvel;

def cambiar_casa_strange(lista:List[SuperHeroe], casa:str):
    ubicacion = lista.search("Dr. Strange", "nombre")
    lista[ubicacion].set_casa(casa)

#   d. mostrar el nombre de aquellos superhéroes que en su biografa menciona la palabra
#      “traje” o “armadura”;

def personajes_con_armadura(lista:List[SuperHeroe]):
    i = 0
    while i < lista.size():
        if "traje" in lista[i].get_biografia() or "armadura" in lista[i].get_biografia():
            print(lista[i])
        i+=1

#   e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#      sea anterior a 1963;

def superheroes_pre_anio(lista:List[SuperHeroe], anio:int):
    lista.sort_by_criterion("anio")
    i = 0

    while i < lista.size() and lista[i].get_anio_aparicion() < anio:
        print(f"Nombre: {lista[i].get_nombre()} | {lista[i].get_casa()}")
        i += 1


#   f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
def casa_cap_marvel_mujer_maravilla(lista:List):
    ubicacion = lista.search("Capitana Marvel","nombre")
    if ubicacion:
        print(f"Casa de Capitana Marvel: {lista[ubicacion].get_casa()}")
    ubicacion = lista.search("Mujer Maravilla","nombre")
    if ubicacion:
        print(f"Casa de Mujer Maravilla: {lista[ubicacion].get_casa()}")


#   h. listar los superhéroes que comienzan con la letra B, M y S;
def superheroes_start_with(lista:List, letras:str):
    i = 0
    while i< lista.size():
        if lista[i].get_nombre().startswith(letras):
            print(lista[i])
        i += 1

#   i. determinar cuántos superhéroes hay de cada casa de comic.
def contador_por_casa(lista:List, casa:str):
    contador = 0
    i = 0
    while i< lista.size():
        if lista[i].get_casa() == casa:
            contador +=1
        i += 1
    return contador

#main

print("Lista Origninal")
lista_de_superheroes.show()
print("")

print("Lista Sin Linterna Verde")
eliminar_linterna_verde(lista_de_superheroes)
lista_de_superheroes.show()
print("")


anio_wolverine =obtener_anio_wolverine(lista_de_superheroes)

if anio_wolverine:
    print(f"Año de Aparicion de Wolverine: {anio_wolverine}")
else:
    print("Wolverine no se encontro en la lista")
print("")


print("Strange con casa cambiada")

cambiar_casa_strange(lista_de_superheroes,"Marvel")
print(lista_de_superheroes[lista_de_superheroes.search("Dr. Strange", "nombre")])
print("")

print("Personajes con armadura/traje")
personajes_con_armadura(lista_de_superheroes)
print("")

print("Personajes pre 1963")
superheroes_pre_anio(lista_de_superheroes, 1963)
print("")

print("Casas de Capitana marvel y Mujer Maravilla:")
casa_cap_marvel_mujer_maravilla(lista_de_superheroes)    
print("")

#   g. mostrar toda la información de Flash y Star-Lord;

print("Informacion de Star-Lord")
print(lista_de_superheroes[lista_de_superheroes.search("Star-Lord", "nombre")])
print("")

print("Informacion de Flash")
print(lista_de_superheroes[lista_de_superheroes.search("Flash", "nombre")])
print("")

print("Superheroes que comienzan con 'B', 'S' o 'M':")
superheroes_start_with(lista_de_superheroes, "B")
superheroes_start_with(lista_de_superheroes, "S")
superheroes_start_with(lista_de_superheroes, "M")

print("")

print(f"Cantidad de personajes de DC: {contador_por_casa(lista_de_superheroes, 'DC')}")
print("")

print(f"Cantidad de personajes de Marvel: {contador_por_casa(lista_de_superheroes, 'Marvel')}")
print("")