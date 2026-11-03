from graph import Graph
from stack import Stack
from typing import Any

# A)
# other_values guarda los episodios del personaje; el peso de la arista son los episodios en comun
# (nombres sin guion porque kruskal usa '-' como separador)

grafo = Graph(False)

PERSONAJES = [
    ("Luke Skywalker", [4, 5, 6, 7, 8, 9]),
    ("Darth Vader", [3, 4, 5, 6]),
    ("Yoda", [1, 2, 3, 5, 6, 8]),
    ("Boba Fett", [2, 5, 6]),
    ("C3PO", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ("Leia", [3, 4, 5, 6, 7, 8, 9]),
    ("Rey", [7, 8, 9]),
    ("Kylo Ren", [7, 8, 9]),
    ("Chewbacca", [3, 4, 5, 6, 7, 8, 9]),
    ("Han Solo", [4, 5, 6, 7, 9]),
    ("R2D2", [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ("BB8", [7, 8, 9]),
]

for personaje in PERSONAJES:
    grafo.add_vertex(personaje[0], personaje[1])


def episodios_en_comun(episodios_a: list, episodios_b: list) -> int:
    cantidad = 0
    for episodio in episodios_a:
        if episodio in episodios_b:
            cantidad += 1
    return cantidad


for i in range(len(PERSONAJES)):
    for j in range(i + 1, len(PERSONAJES)):
        peso = episodios_en_comun(PERSONAJES[i][1], PERSONAJES[j][1])
        if peso > 0:
            grafo.add_edge(peso, PERSONAJES[i][0], PERSONAJES[j][0])

# grafo.show()

# B) Arbol de expansion minimo desde C3PO, Yoda y Leia

def MST_to_triplets_list(mst: str):
    result = []
    for i in mst.split(";"):
        result.append(i.split("-"))
    return result


for origen in ["C3PO", "Yoda", "Leia"]:
    arbol_exp_min = grafo.kruskal(origen)
    print(f"Arbol de expansion minimo desde {origen}:")
    for triplete in MST_to_triplets_list(arbol_exp_min):
        print(f"  {triplete[0]} - {triplete[1]} ({triplete[2]} episodios en comun)")
    print()

# C) Numero maximo de episodios compartidos y pares de personajes que lo cumplen

def maximo_episodios_compartidos(graph: Graph):
    maximo = 0
    for vertex in graph:
        for edge in vertex.edges:
            if edge.weight > maximo:
                maximo = edge.weight

    pares = []
    for vertex in graph:
        for edge in vertex.edges:
            if edge.weight == maximo and vertex.value < edge.destination:
                pares.append((vertex.value, edge.destination))

    return maximo, pares


maximo, pares = maximo_episodios_compartidos(grafo)
print(f"Numero maximo de episodios compartidos: {maximo}")
for par in pares:
    print(f"  {par[0]} y {par[1]}")
print()

# D) Camino mas corto desde C3PO a R2D2 y desde Yoda a Darth Vader

def find_path_dijkstra(paths: Stack, origin: Any, destination: Any):
    target = destination
    path = []

    while (paths.size() > 0):
        if (paths.top_of()[0] != target):
            paths.pop()
        else:
            edge = paths.pop()
            path.append(edge[0])
            target = edge[2]

    path.reverse()
    return path


def cost_from_origin_to_destination(grap: Graph, origin: Any, destination: Any):
    dijkstra_path = grap.dijkstra(origin)
    while (dijkstra_path.size() > 0):
        value, cost, _ = dijkstra_path.pop()
        if value == destination:
            return cost


for origen, destino in [("C3PO", "R2D2"), ("Yoda", "Darth Vader")]:
    todos_los_caminos = grafo.dijkstra(origen)
    camino = find_path_dijkstra(todos_los_caminos, origen, destino)
    costo = cost_from_origin_to_destination(grafo, origen, destino)
    print(f"Camino mas corto desde {origen} a {destino} (total {costo}):")
    print(camino)
    print()

# E) Personajes que aparecieron en los nueve episodios

def personajes_en_todos_los_episodios(graph: Graph, total_episodios: int):
    resultado = []
    for vertex in graph:
        if len(vertex.other_values) == total_episodios:
            resultado.append(vertex.value)
    return resultado


print("Personajes que aparecieron en los nueve episodios:")
for nombre in personajes_en_todos_los_episodios(grafo, 9):
    print(f"  {nombre}")
