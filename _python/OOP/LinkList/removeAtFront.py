class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, value):
        new_node = Node(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def display(self):
        runner = self.head
        list = []
        while (runner):
            list.append(runner.value)
            runner = runner.next
        print(list)
        return self
        
    def remove_from_front(self):
        if self.head is None:
            return None
        self.head = self.head.next
        return self.head
        

myList = LinkedList()
myList.add_to_front(3).add_to_front(3883).add_to_front("kkkk").display()
myList.remove_from_front()
myList.display()