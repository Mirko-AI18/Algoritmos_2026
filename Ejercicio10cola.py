from datetime import time



class Stack:
    def __init__(self):
        self.__elementos = []

    def push(self, dato):
        self.__elementos.append(dato)

    def pop(self):
        return self.__elementos.pop()

    def top(self):
        return self.__elementos[-1]

    def size(self):
        return len(self.__elementos)

    def is_empty(self):
        return len(self.__elementos) == 0

    def show(self):
        for e in reversed(self.__elementos):
            print(e)


class Queue:
    def __init__(self):
        self.__elementos = []

    def arrive(self, dato):
        self.__elementos.append(dato)

    def attention(self):
        return self.__elementos.pop(0)

    def on_front(self):
        return self.__elementos[0]

    def move_to_end(self):
        self.__elementos.append(self.__elementos.pop(0))

    def size(self):
        return len(self.__elementos)

    def is_empty(self):
        return len(self.__elementos) == 0

    def show(self):
        for e in self.__elementos:
            print(e)



#  CLASE NOTIFICACION


class Notificacion:
    def __init__(self, hora, minuto, aplicacion, mensaje):
        self.hora = time(hora, minuto)
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.hora} - {self.aplicacion}: {self.mensaje}"



#  DATOS


datosss = [
    (10, 30, "Facebook",  "Mensaje 1"),
    (11, 45, "Twitter",   "Python es genial"),
    (14, 20, "Instagram", "Mensaje 3"),
    (12,  0, "Spotify",   "Paga spotify premium"),
    ( 9, 15, "Facebook",  "Tu amigo comentó tu foto"),
    (10, 30, "Twitter",   "Python 4.0 fue anunciado hoy"),
    (11, 43, "Instagram", "Nueva historia de un seguidor"),
    (11, 50, "Facebook",  "Tienes un nuevo mensaje"),
    (12, 10, "YouTube",   "Nuevo video de tu canal favorito"),
    (23, 25, "Twitter",   "Python es el lenguaje del futuro"),
    (14, 40, "YouTube",   "Tu video alcanzó 1000 vistas"),
    (15,  0, "Facebook",  "Tienes una nueva solicitud de amistad"),
    (15, 30, "Twitter",   "Alguien retuiteó tu Python tip"),
    (16, 20, "Instagram", "Te mencionaron en una historia"),
]




def cargar(cola):
    for hora, minuto, aplicacion, mensaje in datosss:
        cola.arrive(Notificacion(hora, minuto, aplicacion, mensaje))


# a. Elimina todas las notificaciones de Facebook
def eliminar_facebook(cola: Queue):
    total = cola.size()          # guardamos el tamaño antes de modificar
    for _ in range(total):
        noti = cola.on_front()
        if noti.aplicacion == "Facebook":
            cola.attention()     # la elimina
        else:
            cola.move_to_end()   # la deja al final


# b. Muestra notificaciones de Twitter que incluyan "Python" sin perder datos
def mostrar_twitter_python(cola: Queue):
    for _ in range(cola.size()):
        noti = cola.on_front()
        if noti.aplicacion == "Twitter" and "Python" in noti.mensaje:
            print(noti)
        cola.move_to_end()       # siempre la devuelve al final asi no se pierde nada


# c. Apilaa en una pila las notificaciones entre 11:43 y 15:57 
#    y mostrar cuántas son
def apilar_por_horario(cola: Queue):
    pila = Stack()
    for _ in range(cola.size()):
        noti = cola.on_front()
        if time(11, 43) < noti.hora < time(15, 57):
            pila.push(noti)
        cola.move_to_end()

    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {pila.size()}")
    print("--- Contenido de la pila (de arriba hacia abajo) ---")
    pila.show()



#  PROGRAMA PRINCIPAL


cola = Queue()
cargar(cola)

print("=" * 50)
print("b. Notificaciones de Twitter con la palabra 'Python' (sin perder datos):")
print("=" * 50)
mostrar_twitter_python(cola)

print()
print("=" * 50)
print("Cola completa (sin modificar):")
print("=" * 50)
cola.show()

print()
print("=" * 50)
print("c. Pila con notificaciones entre 11:43 y 15:57:")
print("=" * 50)
apilar_por_horario(cola)

print()
print("=" * 50)
print("a. Cola sin notificaciones de Facebook:")
print("=" * 50)
eliminar_facebook(cola)
cola.show()





# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.