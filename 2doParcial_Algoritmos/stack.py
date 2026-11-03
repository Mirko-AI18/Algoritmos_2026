class Stack:

    def __init__(self):
        self.__elements = []
    
    def push(self,element: any):
        self.__elements.append(element)
    
    def pop(self)-> any:
        return self.__elements.pop()
    
    def top_of(self)-> any:
        return self.__elements[-1]
    
    def size(self)-> int:
        return len(self.__elements)
    
    def show(self):
        stack_aux = Stack()
        print("stack:")
        while self.size() > 0:
            value = self.pop()
            stack_aux.push(value)
            print(value)
    
        while stack_aux.size() > 0:
            value = stack_aux.pop()
            self.push(value)
