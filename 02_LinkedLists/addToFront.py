class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addToFront(self, value):
        new_node = Node(value)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def display(self):
        runner = self.head
        list =[]
        while runner:
            list.append(runner.value)
            runner = runner.next
        print(list)
        return self


my_list = LinkedList()
my_list.addToFront(29).addToFront(34).addToFront(3).display()

        
