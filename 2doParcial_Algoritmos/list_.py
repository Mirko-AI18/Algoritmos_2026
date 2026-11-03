from typing import Any, Optional

class List(list):

    __CRITERION_FUNCTION = {}       #Diccionario donde se almacena 
                                    #                             clave: Nombre del criterio (normalmente el nombre del atributo por el cual ordenar)
                                    #                             valor: Funcion "by_atribute", la cual es definida fuera (en el main por ejemplo) 
                                    #                                    Ejemplo de función:                def by_name(item):
                                    #                                                                           return item.get_name()

    def add_criterion(self, criterion_key, criterion_function) -> None: # Se pide la clave a almacenar, y la función que le corresponde. Las almacena en el diccionario __CRITERION_FUNCTION
        self.__CRITERION_FUNCTION[criterion_key] = criterion_function

    def delete_value(self, value, criterion:str = None) -> Optional[Any]:  # Pide el elemento que se desea borrar, y en base a que atributo se ordenara/buscara la lista (la clave)
        """Elimina un elemento de la lista, utilizando el criterio pasado por parametro, si no se pasa ningun criterio, busca por el valor de los elementos (datos primitivos), si el criterio no se encuentra en la lista de criterios, no realiza la busqueda
        args:
            value: valor del elemento a eliminar
            criterion: clave del criterio por el cual se quiere buscar el elemento, debe ser una de las claves almacenadas en el diccionario __CRITERION_FUNCTION. Si no se pasa ningun criterio, se buscara por el valor de los elementos (datos primitivos)
        """
        index = self.search(value, criterion)                              # Se hace la busqueda del elemento
        return self.pop(index) if index is not None else None              # Devuelve el el elemento eliminado en caso de que exista, si no devuelve None

    def search(self, search_value: Any, criterion:str=None) -> int:        
        """Busca un elemento en la lista mediante busqueda binaria, utilizando el criterio pasado por parametro, si no se pasa ningun criterio, busca por el valor de los elementos (datos primitivos), si el criterio no se encuentra en la lista de criterios, no realiza la busqueda 
        args:
            search_value: valor del elemento a buscar
            criterion: clave del criterio por el cual se quiere buscar el elemento, debe ser una de las claves almacenadas en el diccionario __CRITERION_FUNCTION. Si no se pasa ningun criterio, se buscara por el valor de los elementos (datos primitivos)
        return:          
            indice del elemento buscado, o None si no se encuentra el elemento o el criterio no se encuentra en la lista de criterios
        """
        self.sort_by_criterion(criterion)
        search_criterion = self.__CRITERION_FUNCTION.get(criterion)

        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:

            if search_criterion is None and not isinstance(self[0], (bool,int,float,str)):
                print('No se pudo determinar el criterio de busqueda')
                return None

            value = search_criterion(self[middle]) if search_criterion else self[middle]
            
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1  
            else:
                end = middle - 1

            middle = (start + end) // 2
        

    def insert_value(self, index, value):
        """Inserta un elemento en la lista en la posicion dada por index"""
        self.insert(index, value)

    def sort_by_criterion(self, key_criterion=None) -> None:
        '''Ordena la lista segun el criterio pasado por parametro, si no se pasa ningun criterio, ordena por el valor de los elementos (datos primitivos), si el criterio no se encuentra en la lista de criterios, no ordena la lista
        args:
            key_criterion: clave del criterio por el cual se quiere ordenar la lista, debe ser una de las claves almacenadas en el diccionario __CRITERION_FUNCTION. Si no se pasa ningun criterio, se ordenara por el valor de los elementos (datos primitivos)
        '''
        sort_criterion = self.__CRITERION_FUNCTION.get(key_criterion)
            
        if sort_criterion:
            self.sort(key=sort_criterion)
        elif self and isinstance(self[0], (bool, int, str, float)):  #Checkea si self no esta vacio y si es instancia o no de una clase
            self.sort()
        else:                               
            print ("No se puede realizar el ordenamiento")

    def show(self) -> None:
        """Muestra los elementos de la lista"""
        for element in self:
            print(element)
            
    def size(self) -> int:
        """Devuelve el tamaño de la lista"""
        return len(self)
            
    
