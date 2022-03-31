from pyparsing import null_debug_action


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def insertNodeToEnd(self, data):

        node = Node(data)

        if self.head is None:
            self.head = node
            return self.head

        current = self.head 
        while current.next:
            current = current.next 

        current.next = node 
        return self.head 

    def reversePrint(self, node):

        if node is None:
            return 

        self.reversePrint(node.next)
        print(str(node.data) + '-->', end='')
        
    def reverseLinkedList(self):
        """
        Initialise prev = null, current = head, next = null

        Iterate over linkedlist:
            next = current.next 
            current.next = prev
            prev = current # move one step further 
            current = next 
        """

        current = self.head 
        prev = None
        next = None

        while current:
            next = current.next 
            current.next = prev
            prev = current
            current = next 

        self.head = prev

    def reverseLinkedListRecursive(self, node):

        if node.next is None:
            self.head = node
            return 

        self.reverseLinkedListRecursive(node.next)
        node.next = node 
        

    def printLinkedList(self):
        current = self.head 
        while current:
            print(str(current.data) + '-->', end='')
            current = current.next 

        

if __name__ == '__main__':
    head = LinkedList()
    head.insertNodeToEnd(1)
    head.insertNodeToEnd(2)
    head.insertNodeToEnd(3)
    #head.printLinkedList()
    #print()
    head.reverseLinkedListRecursive(head.head)
    head.printLinkedList()