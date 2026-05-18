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


OPUESTO = {
    "norte":    "sur",
    "sur":      "norte",
    "este":     "oeste",
    "oeste":    "este",
    "noreste":  "suroeste",
    "noroeste": "sureste",
    "sureste":  "noroeste",
    "suroeste": "noreste",
}


DIRECCIONES_VALIDAS = list(OPUESTO.keys())

def registrar_movimientos():
    pila = Pila()

    print("=== REGISTRO DE MOVIMIENTOS DEL ROBOT ===")
    print("Direcciones válidas:", ", ".join(DIRECCIONES_VALIDAS))
    print("Escribí 'fin' para terminar.\n")

    while True:
        direccion = input("Dirección: ").strip().lower()
        if direccion == "fin":
            break
        if direccion not in DIRECCIONES_VALIDAS:
            print("  Dirección inválida, intentá de nuevo.")
            continue

        try:
            pasos = int(input("Pasos: ").strip())
            if pasos <= 0:
                print("  Los pasos deben ser un número positivo.")
                continue
        except ValueError:
            print("  Ingresá un número entero.")
            continue

        pila.push((pasos, direccion))
        print(f"  Movimiento registrado: {pasos} paso(s) hacia el {direccion}\n")

    return pila


def generar_regreso(pila_movimientos):
    print("\n=== SECUENCIA DE REGRESO ===")

    if pila_movimientos.isEmpty():
        print("No hay movimientos registrados.")
        return

    paso_num = 1
    while not pila_movimientos.isEmpty():
        pasos, direccion = pila_movimientos.pop()
        direccion_regreso = OPUESTO[direccion]
        print(f"  Paso {paso_num}: {pasos} paso(s) hacia el {direccion_regreso}")
        paso_num += 1

    print("\nEl robot llegó al punto de partida.")


if __name__ == "__main__":
    pila = registrar_movimientos()

    print(f"\nMovimientos registrados: {pila.size()}")

    generar_regreso(pila)