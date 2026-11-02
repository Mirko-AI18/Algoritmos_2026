from typing import Any, Optional
from queue_ import Queue

class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0

    def get_value(self):
        return self.value
    
    def get_right(self):
            return self.right

    def get_left(self):
            return self.left
    
    def __str__(self):
        return str(self.value)

class BinaryTree():

    def __init__(self):
            self.root = None

    def height(self, root)->int:
        if root is None:
            return -1
        else:
            return root.height

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                root = Node(value, other_value)
            elif value < root.value:
                root.left = __insert_node(root.left, value, other_value)
            else:
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root

        self.root = __insert_node(self.root, value, other_value)




    def delete_node(self, value: Any) -> Optional[Any]:
        def __replace(root):
            if root.right is None:
                return root.left, root
            root.right, aux = __replace(root.right)
            root = self.auto_balance(root)
            self.update_height(root)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    root.left, x, other_value = __delete_node(root.left,value)
                elif value > root.value:
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    x = root.value
                    other_value = root.other_values
                    aux = None
                    if root.left is None:
                        return root.right, x, other_value
                    elif root.right is None:
                        return root.left, x, other_value
                    else:
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values

            root = self.auto_balance(root)
            self.update_height(root)
            return root, x, other_value

        other_value = None
        self.root, x, other_value = __delete_node(self.root, value)

        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:

                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux

        node = __search(self.root, value)

        return node

# Barrido Creciente Plantilla
    def inorden(self) -> None:

        def __inorden(root):
            if root.left is not None:
                __inorden(root.left)
            print(root.value)
            if root.right is not None:
                __inorden(root.right)

        __inorden(self.root)

# Barrido Decreciente Plantilla

    def postorden(self) -> None:

        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

# ?
    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

# Barrido Por Capa Plantilla
    def by_level(self) -> None:
        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)

            lvl = 0
            while(pendings.size()>0):
                print(f"Nivel {lvl}: ")

                for i in range(pendings.size()):
                    node = pendings.attention()
                    print(node.value)
                    if node.left is not None:
                        pendings.arrive(node.left)
                    if node.right is not None:
                        pendings.arrive(node.right)
                lvl += 1

# Auto balanceo

    def update_height(self, root):
        if root is not None:
            root.height = 1 + max(self.height(root.left), self.height(root.right))

    def simple_rotation(self, root, control):
        if control: # rotaicon hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root


    # def altura(self)->int:

    #     def __altura(node):

    #         if (node is not None):
    #             porIz = 0
    #             porDer = 0
    #             if (node.left is not None):
    #                 porIz = 1 + __altura(node.left)
    #             if (node.right is not None):
    #                 porDer = 1 + __altura(node.right)

    #             if porIz > porDer:
    #                 return porIz
    #             else:
    #                 return porDer
    #         return 0

    #     count = __altura(self.root)
    #     return count

    # def by_level(self) -> None:

    #         pendings = Queue()

    #         if self.root is not None:
    #             pendings.arrive(self.root)

    #             while (pendings.size() > 0):
    #                 node = pendings.attention()
    #                 print(node.value)
    #                 if node.left is not None:
    #                     pendings.arrive(node.left)
    #                 if node.right is not None:
    #                     pendings.arrive(node.right)
