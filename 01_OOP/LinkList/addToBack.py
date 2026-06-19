class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_to_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node

        else:
            runner = self.head
            while runner.next:
                runner = runner.next 
            runner.next = new_node

    def display(self):
        runner = self.head
        list = []
        while runner:
            list.append(runner.value)
            runner = runner.next
        print(list)


my_list = LinkedList()
my_list.add_to_back(83)
my_list.add_to_back(9)
my_list.add_to_back(4)
my_list.add_to_back(21)
my_list.display()