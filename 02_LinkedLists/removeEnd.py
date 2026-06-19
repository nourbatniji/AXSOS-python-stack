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
            return
        else:
            runner = self.head
            while runner.next:
                runner = runner.next
            runner.next = new_node
            return
        
    def remove_end(self):
        runner = self.head
        while runner.next.next: #bc we need to stop at the second to last node
            runner = runner.next
        runner.next = None
    
    def display(self):
        runner = self.head
        list = []
        while runner:
            list.append(runner.value)
            runner = runner.next
        print(list)
        return
    

mylist = LinkedList()
mylist.add_to_back(38)
mylist.add_to_back(8)
mylist.add_to_back(3)
mylist.add_to_back(112)
mylist.remove_end()
mylist.display()
        