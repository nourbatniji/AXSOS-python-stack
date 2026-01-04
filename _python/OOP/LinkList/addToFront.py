class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head #the next is the current head
        self.head = new_node # the first value of the new node is at the head
        return self
      

    def display(self):
        runner = self.head
        list = []
        while (runner):
            list.append(runner.value)
            runner = runner.next
        print(list)

my_list = LinkedList()
my_list.add_to_front(3)
my_list.add_to_front(2)
my_list.add_to_front(4)
my_list.add_to_front(1)
my_list.display()