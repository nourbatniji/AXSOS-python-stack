class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            runner = self.head
            while runner.next:
                runner = runner.next
            runner.next = new_node
            return

    def display(self):
        runner = self.head
        list = []
        while runner.next:
            list.append(runner.value)
            runner = runner.next
        print(list)
        return
    
my_list = LinkedList()
my_list.add_to_end(888)
my_list.add_to_end(2)
my_list.add_to_end(8)
my_list.add_to_end(1)
my_list.display()