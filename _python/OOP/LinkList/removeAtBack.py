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


    def remove_from_back(self):
        runner = self.head

        while (runner.next.next != None):
            runner = runner.next
        runner.next = None
    
    def display(self):
        runner = self.head
        list = []
        while (runner):
            list.append(runner.value)
            runner = runner.next
        print(list)
        
        
my_list = LinkedList() 
my_list.add_to_front(2)
my_list.add_to_front(32)
my_list.add_to_front(4)
my_list.remove_from_back()  
my_list.display()  