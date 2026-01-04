class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addtofront(self, value):
        newnode = Node(value)
        currenthead = self.head
        newnode.next = currenthead
        self.head = newnode

    def removeval(self, value):
        runner = self.head
        found = False

        if runner == None:
            print("List is Empty!")
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
            print("not found")


    def display(self):
        runner = self.head
        list =[]
        while runner:
            list.append(runner.value)
            runner = runner.next
        print(list)



list = LinkedList()
list.addtofront(38)
list.addtofront(98)
list.addtofront(7)
list.addtofront(4)
list.removeval(100000)
list.display()

    