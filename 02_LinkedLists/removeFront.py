class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addToBack(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        else:
            runner = self.head
            while runner.next:
                runner = runner.next
            runner.next = new_node

    def removeFront(self):
        if self.head is None:
            return None
        self.head = self.head.next
        return self.head
    
    def display(self):
        runner = self.head
        list = []
        while runner:
            list.append(runner.value)
            runner = runner.next
        print(list)
        return
    
my_list = LinkedList()
my_list.addToBack(93)
my_list.addToBack(3)
my_list.addToBack(9)
my_list.addToBack(22)
my_list.removeFront()
my_list.display()