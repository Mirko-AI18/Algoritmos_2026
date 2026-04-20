print("Ejercicio 22")

def usar_la_fuerza(mochila, objetos_sacados=0):
    
   
    if len(mochila) == 0:
        return "No se encontró un sable de luz", objetos_sacados

    
    objeto = mochila[0]

   
    if objeto == "sable de luz":
        return "Se encontró un sable de luz", objetos_sacados + 1

   
    return usar_la_fuerza(mochila[1:], objetos_sacados + 1)



mochila_jedi = [
    "comida",
    "ropa",
    "mapa estelar",
    "comunicador",
    "sable de luz",
    "botiquin"
]

resultado, cantidad = usar_la_fuerza(mochila_jedi)

print(resultado)
print("Objetos sacados:", cantidad)

