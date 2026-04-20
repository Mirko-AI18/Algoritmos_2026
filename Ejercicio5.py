
print("Ejercicio 5")

def romano_decimal(romano: str) -> int:
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if romano == "":
        return 0

    if len(romano) == 1:
        return valores[romano]

    primero = valores[romano[0]]
    segundo = valores[romano[1]]

    if primero < segundo:
        return -primero + romano_decimal(romano[1:])
    else:
        return primero + romano_decimal(romano[1:])
    
print(romano_decimal("X"))

# romano(N) = valor(actual) +/- romano(resto) -> romano("")=0, romano("X")=10