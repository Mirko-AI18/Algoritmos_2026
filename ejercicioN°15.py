# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, 
# cantidad de batallas perdidas y cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: 
# nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades utilizando lista de lista implementando las 
# funciones necesarias:
# 
#    a. obtener la cantidad de Pokémons de un determinado entrenador;
#    
#    b. listar los entrenadores que hayan ganado más de tres torneos;[115]
#    
#    c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#    
#    d. mostrar todos los datos de un entrenador y sus Pokémos;
#    
#    e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#    
#    f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#    (tipo y subtipo);
#    
#    g. el promedio de nivel de los Pokémons de un determinado entrenador;
#    
#    h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#    
#    i. mostrar los entrenadores que tienen Pokémons repetidos;
#    
#    j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
#    
#    k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#    como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#    deberán mostrar los datos de ambos;


from list_ import List

class Pokemon:
    def __init__(self, nombre:str, nivel:int, tipo:str, subtipo:str):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__tipo = tipo
        self.__subtipo = subtipo

    def get_nombre(self):
        return self.__nombre

    def get_nivel(self):
        return self.__nivel

    def get_tipo(self):
        return self.__tipo

    def get_subtipo(self):
        return self.__subtipo

    def __str__(self):
        return f"Nombre: {self.__nombre}, \nNivel: {self.__nivel}, \nTipo: {self.__tipo}, \nSubtipo: {self.__subtipo}"


class Trainer:
    def __init__(self, nombre:str, torneos_ganados:int, batallas_perdidas:int, batallas_ganadas:int):
        self.__nombre = nombre
        self.__torneos_ganados = torneos_ganados
        self.__batallas_perdidas = batallas_perdidas
        self.__batallas_ganadas = batallas_ganadas
        self.__pokemons = List()

        # Agregar criterios de busqueda para los pokemon
        def by_nivel(pokemon: Pokemon):
            return pokemon.get_nivel()
        self.__pokemons.add_criterion("nivel", by_nivel)

    def get_nombre(self):
        return self.__nombre

    def get_torneos_ganados(self):
        return self.__torneos_ganados

    def get_batallas_perdidas(self):
        return self.__batallas_perdidas

    def get_batallas_ganadas(self):
        return self.__batallas_ganadas

    def get_pokemons(self):
        return self.__pokemons

    def add_pokemon(self, *pokemon:Pokemon):
        new_pokemon = len(pokemon)

        if new_pokemon == 0:
            print("No se agregaron Pokemons")
            return

        if self.__pokemons.size() + new_pokemon > 6:
            print(f"No se pueden agregar tantos Pokemons, el entrenador ya tiene {self.__pokemons.size()} Pokemons")
            return

        for p in pokemon:
            self.__pokemons.append(p)
    def __str__(self):
        return f"Nombre: {self.__nombre}, \nTorneos Ganados: {self.__torneos_ganados}, \nBatallas Perdidas: {self.__batallas_perdidas}, \nBatallas Ganadas: {self.__batallas_ganadas}"



# Agregar Entrenadores a las lista

entrenadores = List()

entrenadores.append(Trainer("Ash Ketchum", 5, 10, 50))
entrenadores.append(Trainer("Misty", 2, 5, 20))
entrenadores.append(Trainer("Brock", 4, 8, 30))
entrenadores.append(Trainer("Gary Oak", 6, 12, 60))
entrenadores.append(Trainer("Dawn", 3, 7, 25))
entrenadores.append(Trainer("May", 1, 3, 15))
entrenadores.append(Trainer("Profesor Oak", 10, 20, 120))

# Agregar Pokémons a los entrenadores
for entrenador in entrenadores:
    if entrenador.get_nombre() == "Ash Ketchum":
        entrenador.add_pokemon(Pokemon("Pikachu", 50, "Eléctrico", "Normal"), Pokemon("Charizard", 70, "Fuego", "Volador"), Pokemon("Bulbasaur", 40, "Planta", "Veneno"))
    elif entrenador.get_nombre() == "Misty":
        entrenador.add_pokemon(Pokemon("Starmie", 60, "Agua", "Psíquico"), Pokemon("Psyduck", 40, "Agua", "Normal"))
    elif entrenador.get_nombre() == "Brock":
        entrenador.add_pokemon(Pokemon("Onix", 55, "Roca", "Tierra"), Pokemon("Geodude", 45, "Roca", "Tierra"))
    elif entrenador.get_nombre() == "Gary Oak":
        entrenador.add_pokemon(Pokemon("Blastoise", 75, "Agua", "Normal"), Pokemon("Arcanine", 65, "Fuego", "Normal"), Pokemon("Alakazam", 70, "Psíquico", "Normal"), Pokemon("Gyarados", 80, "Agua", "Volador"), Pokemon("Scovillain", 65, "Fuego", "Planta"))
    elif entrenador.get_nombre() == "Dawn":
        entrenador.add_pokemon(Pokemon("Piplup", 50, "Agua", "Normal"), Pokemon("Buneary", 45, "Normal", "Normal"), Pokemon("Wingull", 55, "Agua", "Volador"))
    elif entrenador.get_nombre() == "May":
        entrenador.add_pokemon(Pokemon("Torchic", 50, "Fuego", "Normal"), Pokemon("Treecko", 45, "Planta", "Normal"), Pokemon("Wingull", 55, "Agua", "Volador"))
    elif entrenador.get_nombre() == "Profesor Oak":
        entrenador.add_pokemon(Pokemon("Tyrantrum", 30, "Roca", "Dragon"), Pokemon("Terrakion", 25, "Roca", "Lucha"), Pokemon("Mew", 90, "Psiquico", "None"))
# Añadir criterios de busqueda
def by_nombre(entrenador: Trainer):
    return entrenador.get_nombre()

entrenadores.add_criterion("nombre", by_nombre)

def by_torneos_ganados(entrenador: Trainer):
    return entrenador.get_torneos_ganados()

entrenadores.add_criterion("torneos_ganados", by_torneos_ganados)

# a. obtener la cantidad de Pokémons de un determinado entrenador;
def obtener_cantidad_pokemons(entrenadores: List[Trainer], nombre_entrenador: str) -> int:
    ubicacion = entrenadores.search(nombre_entrenador, "nombre")
    if ubicacion is not None:
        return (entrenadores[ubicacion].get_pokemons()).size()
    return 0

print("==============================================================================")
print(f"La cantidad de Pokémons de Ash Ketchum es: {obtener_cantidad_pokemons(entrenadores, "Ash Ketchum")}")
print("==============================================================================")
print()
# b. listar los entrenadores que hayan ganado más de tres torneos;
def entrenadores_mas_de_tres_torneos(entrenadores: List[Trainer]):
    i = 0
    while i < entrenadores.size():
        if entrenadores[i].get_torneos_ganados() > 3:
            print(entrenadores[i].get_nombre())
        i += 1

print("==============================================================================")
print("Entrenadores que ganaron más de tres torneos:")
entrenadores_mas_de_tres_torneos(entrenadores)
print("==============================================================================")
print()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def pokemon_mayor_nivel(entrenadores: List[Trainer]):
    entrenadores.sort_by_criterion("torneos_ganados")
    entrenador_top = entrenadores[entrenadores.size() - 1]
    pokemons = entrenador_top.get_pokemons()
    if pokemons.size() == 0:
        print(f"{entrenador_top.get_nombre()} no tiene Pokémons.")
        return
    pokemons.sort_by_criterion("nivel")
    pokemon_top = pokemons[pokemons.size() - 1]
    print(f"El Pokémon de mayor nivel de {entrenador_top.get_nombre()} es {pokemon_top.get_nombre()} con nivel {pokemon_top.get_nivel()}.")

print("==============================================================================")
pokemon_mayor_nivel(entrenadores)
print("==============================================================================")
print()
# d. mostrar todos los datos de un entrenador y sus Pokémos;
def mostrar_datos_entrenador(entrenadores: List[Trainer], nombre_entrenador: str):
    ubicacion = entrenadores.search(nombre_entrenador, "nombre")
    if ubicacion is not None:
        entrenador = entrenadores[ubicacion]
        print(entrenador)
        pokemons = entrenador.get_pokemons()
        if pokemons.size() == 0:
            print(f"{entrenador.get_nombre()} no tiene Pokémons.")
            return
        print()
        print("Pokémons:")
        for pokemon in pokemons:
            print(pokemon)
            print()
    else:
        print(f"No se encontró al entrenador {nombre_entrenador}.")
print("==============================================================================")
print("Datos del entrenador Gary Oak:")
mostrar_datos_entrenador(entrenadores, "Gary Oak")
print("==============================================================================")
print()
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def entrenadores_porcentaje_batallas(entrenadores: List[Trainer], porcentaje: float):
    i = 0
    while i < entrenadores.size():
        entrenador = entrenadores[i]
        total_batallas = entrenador.get_batallas_ganadas() + entrenador.get_batallas_perdidas()
        if total_batallas > 0:
            porcentaje_ganadas = (entrenador.get_batallas_ganadas() / total_batallas) * 100
            if porcentaje_ganadas > porcentaje:
                print(f"{entrenador.get_nombre()} tiene un porcentaje de batallas ganadas de {porcentaje_ganadas:.2f}%")
        i += 1

print("==============================================================================")
entrenadores_porcentaje_batallas(entrenadores, 79)
print("==============================================================================")
print()

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
def entrenadores_tipo_pokemon(entrenadores: List[Trainer], tipo:str, subtipo:str):
    i = 0
    while i < entrenadores.size():
        entrenador = entrenadores[i]
        pokemons = entrenador.get_pokemons()
        tiene_tipo = False
        j = 0
        while j < pokemons.size() and not tiene_tipo:
            pokemon = pokemons[j]
            if (pokemon.get_tipo() == tipo and pokemon.get_subtipo() == subtipo):
                tiene_tipo = True
            j += 1

        if tiene_tipo:
            print(f"{entrenador.get_nombre()} tiene Pokémons de tipo {tipo} y subtipo {subtipo}.")
        i += 1

print("==============================================================================")
entrenadores_tipo_pokemon(entrenadores, "Fuego", "Planta")
entrenadores_tipo_pokemon(entrenadores, "Agua", "Volador")
print("==============================================================================")
print()
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promedio_nivel_pokemons(entrenadores: List[Trainer], nombre_entrenador: str):
    ubicacion = entrenadores.search(nombre_entrenador, "nombre")
    if ubicacion is not None:
        entrenador = entrenadores[ubicacion]
        pokemons = entrenador.get_pokemons()
        if pokemons.size() == 0:
            print(f"{entrenador.get_nombre()} no tiene Pokémons.")
            return
        total_nivel = 0
        i = 0
        while i < pokemons.size():
            total_nivel += pokemons[i].get_nivel()
            i += 1
        promedio = total_nivel / pokemons.size()
        print(f"El promedio de nivel de los Pokémons de {entrenador.get_nombre()} es {promedio:.2f}.")
    else:
        print(f"No se encontró al entrenador {nombre_entrenador}.")

print("==============================================================================")
promedio_nivel_pokemons(entrenadores, "Misty")
print("==============================================================================")
print()
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def entrenadores_con_pokemon(entrenadores: List[Trainer], nombre_pokemon: str):
    contador = 0
    i = 0
    while i < entrenadores.size():
        entrenador = entrenadores[i]
        pokemons = entrenador.get_pokemons()
        j = 0
        while j < pokemons.size():
            if pokemons[j].get_nombre() == nombre_pokemon:
                contador += 1
                break
            j += 1
        i += 1
    print(f"{contador} entrenador/es tiene/n al Pokémon {nombre_pokemon}.")

print("==============================================================================")
entrenadores_con_pokemon(entrenadores, "Pikachu")
entrenadores_con_pokemon(entrenadores, "Wingull")
print("==============================================================================")
print()

# i. listar todos los Pokémons de un determinado entrenador;
def listar_pokemons_entrenador(entrenadores: List[Trainer], nombre_entrenador: str):
    ubicacion = entrenadores.search(nombre_entrenador, "nombre")
    if ubicacion is not None:
        entrenador = entrenadores[ubicacion]
        pokemons = entrenador.get_pokemons()
        print(f"Pokémons de {entrenador.get_nombre()}:")
        i = 0
        while i < pokemons.size():
            pokemon = pokemons[i]
            print(f"{pokemon}")
            print()
            i += 1
    else:
        print(f"No se encontró al entrenador {nombre_entrenador}.")

print("==============================================================================")
listar_pokemons_entrenador(entrenadores, "Gary Oak")
print("==============================================================================")
print()

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
def entrenadores_con_pokemon_especifico(entrenadores: List[Trainer], pokemon_especifico: str):
    i = 0
    while i < entrenadores.size():
        entrenador = entrenadores[i]
        pokemons = entrenador.get_pokemons()
        j = 0
        while j < pokemons.size():
            if pokemons[j].get_nombre() == pokemon_especifico:
                print(f"{entrenador.get_nombre()} tiene al Pokémon {pokemons[j].get_nombre()}.")
                break
            j += 1
        i += 1

print("==============================================================================")
entrenadores_con_pokemon_especifico(entrenadores, "Tyrantrum")
entrenadores_con_pokemon_especifico(entrenadores, "Terrakion")
entrenadores_con_pokemon_especifico(entrenadores, "Wingull")
print("==============================================================================")
print()

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;
def entrenador_tiene_pokemon(entrenadores: List[Trainer], nombre_entrenador: str, nombre_pokemon: str):
    ubicacion = entrenadores.search(nombre_entrenador, "nombre")

    if ubicacion is not None:
        entrenador = entrenadores[ubicacion]
        pokemons = entrenador.get_pokemons()
        i = 0

        while i < pokemons.size():
            if pokemons[i].get_nombre() == nombre_pokemon:
                print(f"{entrenador.get_nombre()} tiene al Pokémon {pokemons[i].get_nombre()}.")
                print(f"Datos del entrenador: \n{entrenador}")
                print()
                print(f"Datos del Pokémon: \n{pokemons[i]}")
                return
            i += 1
        print(f"{entrenador.get_nombre()} no tiene al Pokémon {nombre_pokemon}.")
    else:
        print(f"No se encontró al entrenador {nombre_entrenador}.")

print("==============================================================================")
entrenador_tiene_pokemon(entrenadores, "Ash Ketchum", "Pikachu")
print()
entrenador_tiene_pokemon(entrenadores, "Misty", "Charizard")
print("==============================================================================")