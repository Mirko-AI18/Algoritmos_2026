from typing import Any

class HeapMax():
    def __init__(self):
        self.elements = []

    def add_element(self, value: Any) -> None:
        self.elements.append(value)
        self.float_element(self.size()-1)


    def delete_top_element(self) -> None:
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        value = self.elements.pop()
        self.sink_element(0)

    def size(self) -> int:
        return len(self.elements)

    def float_element(self, index) -> None:
        while index > 0 and (self.elements[index] > self.elements[(index - 1) // 2]):
            father = ((index - 1) // 2)
            self.elements[index], self.elements[father] = self.elements[father], self.elements[index]
            index = father

    def sink_element(self, index) -> None:
        left_child = (index * 2) + 1
        control = True
        while(control and left_child < self.size()):
            right_child = left_child + 1
            aux = left_child
            if (right_child < self.size()):
                if self.elements[right_child] > self.elements[left_child]:
                    aux = right_child

            if self.elements[index] < self.elements[aux]:
                self.elements[index], self.elements[aux] = self.elements[aux], self.elements[index] 
                index = aux
                left_child = (index * 2) + 1
            else:
                control = False

    def convert_to_heap(self)->None:
        for i in range(len(self.elements)):
            self.float_element(i)

    def heap_sort(self)->None:
        result = []
        while self.size() > 0:
            value = self.delete_top_element
            result.append(value)
        return result

class HeapMin():

    def __init__(self):
        self.elements = []


    def add_element(self, value: Any) -> None:
        self.elements.append(value)
        # flotar para restablecer orden si es necesario
        self.float(self.size()-1)

    def delete_top_element(self) -> Any:
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        value = self.elements.pop()
        # hundir para reestablecer orden
        self.sink(0)
        return value

    def size(self) -> int:
        return len(self.elements)

    def float(self, index) -> None:
        # print('intentar flotar')
        while index > 0 and self.elements[index][0] < self.elements[(index -1) // 2][0]:
            father = (index -1) // 2
            # print(f'flotar {index}, {father}')
            self.elements[index], self.elements[father] = self.elements[father], self.elements[index]
            index = father

    def sink(self, index) -> None:
        # print('intentar hundir')
        left = (index * 2) + 1
        control = True
        while control and left < self.size():
            # print(self.elements)
            # input()
            right =  (index * 2) + 2
            min = left
            if right < self.size() and self.elements[right][0] < self.elements[left][0]:
                min = min if self.elements[min] < self.elements[right] else right

            if self.elements[index][0] > self.elements[min][0]:
                # print(f'hundir {index}, {max}')
                self.elements[index], self.elements[min] = self.elements[min], self.elements[index]
                index = min
                left = (index * 2) + 1
            else:
                control = False

    def arrive(self, value, priority) -> None:
        self.add_element([priority, value])

    def search(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def attention(self) -> Any:
        result = None
        if self.size() > 0:
            result = self.delete_top_element()

        return result

    def convert_to_heap(self) -> None:
        for i in range(len(self.elements)):
            self.float(i)

    def heap_sort(self) -> None:
        result = []
        while self.size() > 0:
            value = self.delete_top_element()
            result.append(value)

        return result

    def change_priority(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.sink(index)
            elif new_priority < previous_priority:
                self.float(index)

