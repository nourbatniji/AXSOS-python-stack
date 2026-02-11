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
        
    def removeVal(self, value):
        runner = self.head
        found = False

        if runner is None:
            print("List is Empty")
            return
        
        if runner.value == value:
            self.head = runner.next
            return
        
        while runner.next:
            if runner.next.value == value:
                runner.next = runner.next.next
                return

            runner = runner.next

        if not found:
            print("Not in the list")


    def display(self):
        runner = self.head
        list = []
        while runner:
            list.append(runner.value)
            runner = runner.next
        print(list)
        return

my_list = LinkedList()
my_list.add_to_back(83)
my_list.add_to_back(22)
my_list.add_to_back(11)
my_list.add_to_back(4)
my_list.removeVal(4)
my_list.removeVal(5)
my_list.display()