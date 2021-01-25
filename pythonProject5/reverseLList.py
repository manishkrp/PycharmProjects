# This program reverses the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self,new_data):
         new_node = Node(new_data)
         new_node.next = self.head
         self.head = new_node

    def printLst(self):
         temp = self.head
         while(temp):
             print(temp.data)
             temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.push(60)
llist.push(70)

print("Given linked list:")
llist.printLst()
llist.reverse()
print("\n Reversed linked list:")
llist.printLst
