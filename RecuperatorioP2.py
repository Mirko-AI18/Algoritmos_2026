from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes

class personajes():
    def    __init__ (self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name=name
        self.alias=alias
        self.real_name=real_name
        self.short_bio=short_bio
        self.first_appearance=first_appearance
        self.is_villain=is_villain


    def __str__(self):
            return (
            f"Nombre:       {self.name}\n"
            f"Alias:        {self.alias}\n"
            f"Nombre real:  {self.real_name}\n"
            f"Biografía:    {self.short_bio}\n"
            f"Aparición:    {self.first_appearance}\n"
            f"Villano:      {self.is_villain}\n"
            )


def pornombre(x):
    return(x).name
def pornombrereal(x):
    return(x).real_name or ""
def porfechaapari(x):
    return(x).first_appearance


listacrack=List()

listacrack.add_criterion("name", pornombre)
listacrack.add_criterion("real_name", pornombrereal)
listacrack.add_criterion("first_appearance", porfechaapari)

def cargarsuper(listacrack:List):
    for x in superheroes:
        listacrack.append (personajes(x["name"],x["alias"],x["real_name"],x["short_bio"],x["first_appearance"],x["is_villain"]))


def listascendente(listacrack: List):
    listacrack.sort_by_criterion("name")
    print("Lista de Manera Ascendentes por Nombres de Personajes: ")
    print()
    for x in listacrack:
        print(x.name)

def listarVillanos(listacrack: List):
    print("LISTA DE VILLANOS:")
    print()
    for x in listacrack:
        if x.is_villain == True:
            print(x)


def shearchTT(listacrack: List):
    thing = listacrack.search("The Thing", "name")
    if thing is not None:
        print(f"{listacrack[thing].name} se encontro dentro de la lista en la posicion {thing}")
    else:
        print("no encontrado")

def shearchRR(listacrack: List):
    Rocket = listacrack.search("Rocket Raccoon", "name")
    if Rocket is not None:
        print(f"{listacrack[Rocket].name} se encontro dentro de la lista en la posicion {Rocket}")
        print()
    else:
        print("no encontrado")
        print()

def villanosAntiguos(listacrack: List):
    cola_villanos = Queue()
    for personaje in listacrack:
        if personaje.is_villain == True:
            cola_villanos.arrive(personaje)

    cola_villanos.show()

    print("Villanos con primera aparicion antes de 1980:")
    cantidad = cola_villanos.size()
    for _ in range(cantidad):
        actual = cola_villanos.on_front()
        if actual.first_appearance < 1980:
            print(actual.name)
        cola_villanos.move_to_end()


def listarIniciales(listacrack: List):
    print("personajes que inicien con Bl, G, My o W:")
    print()
    listacrack.filter_start_with(["Bl", "G", "My", "W"])



def listanombrerealAsc(listacrack: List):
    print("lista ordenada por nombre reals ascendente:")
    print()
    listacrack.sort_by_criterion("real_name")
    for personaje in listacrack:
        print(personaje.real_name)


def fechaAparece(listacrack: List):
    print("lista ordenada por fecha de primera aparicion:")
    listacrack.sort_by_criterion("first_appearance")
    for personaje in listacrack:
        print(personaje.name, personaje.first_appearance)


def modificarSL(listacrack: List):
    indice = listacrack.search("Ant Man", "name")
    if indice is not None:
        listacrack[indice].real_name = "Scott Lang"
        print(f"nombre real de  Ant Man actualizado: {listacrack[indice].real_name}")


def contieneBio(listacrack: List):
    print()
    print("personajes con biografias que tengan palabra clave:")
    print()
    listacrack.filter_contain_on_bio(["time-traveling", "suit"])



def eliminar(listacrack: List):
    eliminado_electro = listacrack.delete_value("Electro", "name")
    if eliminado_electro is not None:
        print()
        print(f"se elimino: {eliminado_electro}")
        print()
    else:
        print("Electro no estaba en la lista")
        print()

    eliminado_zemo = listacrack.delete_value("Baron Zemo", "name")
    if eliminado_zemo is not None:
        print(f"se elimino: {eliminado_zemo}")
    else:
        print("Baron Zemo no estaba en la lista")


cargarsuper(listacrack)
listascendente(listacrack)
listarVillanos(listacrack)
shearchTT(listacrack)
shearchRR(listacrack)
villanosAntiguos(listacrack)
listarIniciales(listacrack)
listanombrerealAsc(listacrack)
fechaAparece(listacrack)
modificarSL(listacrack)
contieneBio(listacrack)
eliminar(listacrack)
