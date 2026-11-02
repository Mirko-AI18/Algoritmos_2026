import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tree import BinaryTree

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
    # I. determinar cuántos nodos tiene cada árbol;
    # II. realizar un barrido ordenado alfabéticamente de cada árbol.
    
from super_heroes_data import superheroes

arbol_marvel = BinaryTree()

for personaje in superheroes:
    arbol_marvel.insert_node(personaje['name'], other_value=personaje)
    
    
# b. listar los villanos ordenados alfabéticamente;
arbol_marvel.inorden_villain()

# c. mostrar todos los superhéroes que empiezan con C;
arbol_marvel.inorden_hero_star_with('C')

# d. determinar cuántos superhéroes hay el árbol;
cantidad_heroes = arbol_marvel.count_heroes()
print(f'- cantidad de heroes: {cantidad_heroes}')

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
arbol_marvel.proxy_search('str')

nodo_encontrado = arbol_marvel.search('Dr Strannnnnge')

if nodo_encontrado is not None:
    valor_viejo, datos = arbol_marvel.delete_node(nodo_encontrado.value)
    datos['name'] = 'Dr Strange'
    arbol_marvel.insert_node('Dr Strange', datos)
else:
    print('no se encontró al superhéroe a modificar')
    
# f. listar los superhéroes ordenados de manera descendente;
arbol_marvel.postorden_hero()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

def generar_bosque(nodo):
    if nodo is None:
        return
    if nodo.other_values['is_villain']:
        arbol_villanos.insert_node(nodo.value, nodo.other_values)
    else:
        arbol_heroes.insert_node(nodo.value, nodo.other_values)
    generar_bosque(nodo.left)
    generar_bosque(nodo.right)
    
generar_bosque(arbol_marvel.root)

# I. determinar cuántos nodos tiene cada árbol;
def contar_nodos(nodo):
    if nodo is None:
        return 0
    return 1 + contar_nodos(nodo.left) + contar_nodos(nodo.right)

print(f'nodos en arbol de heroes: {contar_nodos(arbol_heroes.root)}')
print(f'nodos en arbol de villanos: {contar_nodos(arbol_villanos.root)}')
print()

# II. realizar un barrido ordenado alfabéticamente de cada árbol.
arbol_heroes.inorden()
arbol_villanos.inorden()




# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from tabla_ejericio_23 import criaturas

arbol_criaturas = BinaryTree()
for c in criaturas:
    arbol_criaturas.insert_node(c['name'], {'derrotado_por': c['derrotado_por'], 'descripcion': None, 'capturada': None})

# a. listado inorden de las criaturas y quienes la derrotaron;
arbol_criaturas.inorden_criaturas()

# b. se debe permitir cargar una breve descripción sobre cada criatura;
buscar_criatura = input('ingrese el nombre de la criatura: ')
cargar_descripcion = input('ingrese descripcion de la criatura: ')

nodo = arbol_criaturas.search(buscar_criatura)
if nodo is not None:
    nodo.other_values['descripcion'] = cargar_descripcion
    print(nodo.value, nodo.other_values)
else:
    print(f'no se encontro la criatura {buscar_criatura}')
    
# c. mostrar toda la información de la criatura Talos;
nodo_talos = arbol_criaturas.search('Talos')
if nodo_talos is not None:
    print(nodo_talos.value, nodo_talos.other_values)
else:
    print('no se encontro la criatura Talos')
print()

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
conteo = arbol_criaturas.contar_derrotas()

for i in range(3):
    mayor_heroe = None
    mayor_cantidad = 0
    for heroe in conteo:
        if conteo[heroe] > mayor_cantidad:
            mayor_heroe = heroe
            mayor_cantidad = conteo[heroe]
    print(mayor_heroe, mayor_cantidad)
    conteo.pop(mayor_heroe)

print()

# e. listar las criaturas derrotadas por Heracles;
arbol_criaturas.inorden_derrotado_por('Heracles')
print()

# f. listar las criaturas que no han sido derrotadas;
arbol_criaturas.inorden_no_derrotadas()
print()

#g. ya incluido en other_values al cargar el árbol

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
capturados = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']

for nombre in capturados:
    nodo = arbol_criaturas.search(nombre)
    if nodo is not None:
        nodo.other_values['capturada'] = 'Heracles'
        print(nodo.value, nodo.other_values)
    else:
        print(f'no se encontro la criatura {nombre}')
print()

# i. se debe permitir búsquedas por coincidencia;
buscar = input('ingrese texto a buscar: ').lower()
arbol_criaturas.proxy_search(buscar)
print()

# j. eliminar al Basilisco y a las Sirenas;
eliminar = ['Basilisco', 'Sirenas']
for nombre in eliminar:
    valor, datos = arbol_criaturas.delete_node(nombre)
    if valor is not None:
        print(f'se elimino {nombre}')
    else:
        print(f'no se encontro {nombre}')
print()

arbol_criaturas.inorden_criaturas()
print()
print(arbol_criaturas.search('Basilisco'))
print(arbol_criaturas.search('Sirenas'))
print()
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
nodo = arbol_criaturas.search('Aves del Estínfalo')
if nodo is not None:
    nodo.other_values['derrotado_por'] = 'Heracles'
    nodo.other_values['descripcion'] = 'Heracles derroto a varias'
    print(nodo.value, nodo.other_values)
else:
    print('no se encontro la criatura Aves del Estinfa')
print()

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
valor, datos = arbol_criaturas.delete_node('Ladón')
if valor is not None:
    arbol_criaturas.insert_node('Dragón Ladón', datos)
    print(f'se modifico {valor} por Dragón Ladón')
else:
    print('no se encontro la criatura Ladón')
print()
print(arbol_criaturas.search('Ladón'))
print()

# m. realizar un listado por nivel del árbol;
arbol_criaturas.by_level()
print()

# n. muestre las criaturas capturadas por Heracles.
arbol_criaturas.inorden_capturada_por('Heracles')