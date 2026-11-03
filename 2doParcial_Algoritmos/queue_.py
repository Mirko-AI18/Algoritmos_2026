from typing import Any

class Queue:
    def __init__(self):
        self.__elements = []

    def arrive(self, element: Any) -> None:
        self.__elements.append(element)

    def attention(self) -> Any:
        return self.__elements.pop(0)
    
    def size(self) -> int:
        return len(self.__elements)

    def on_front(self) -> Any:
        return self.__elements[0]
    
    def move_to_end(self) -> Any:
        element = self.__elements.pop(0)
        self.__elements.append(element)
        return element


    def show(self):
        size = self.size()
        for i in range (size):
            element = self.move_to_end()
            print(element)
        