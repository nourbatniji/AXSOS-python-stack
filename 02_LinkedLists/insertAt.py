class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at(self, value, position):
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0

        while current is not None and index < position - 1: #keep moving until you reach the indx before the given one
            current = current.next
            index += 1

        new_node.next = current.next
        current.next = new_node
        
        if current is None:
            print("Position out of range")
            return

    def display(self):
        runner = self.head
        list =[]
        while runner:
            list.append(runner.value)
            runner = runner.next
        print(list)


mylist = LinkedList()
mylist.insert_at(10, 0)  
mylist.insert_at(20, 1)  
mylist.insert_at(15, 1)  
mylist.insert_at(5, 0)  
mylist.display()
