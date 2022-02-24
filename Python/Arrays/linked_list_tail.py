class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node
        return

    def print_list(self, head):
        temp = head
        list_str = ''
        if self.head is None:
            return 'None'
        while temp:
            list_str += str(temp.data) + '->'
            temp = temp.next
        list_str += 'None'
        print(list_str)

            
    def construct(self, keys):
        for i in reversed(range(len(keys))):
            key = keys[i]
            self.insert_at_start(key)

class Solution:

    '''
    A singly-linked list node is defined as:

    class Node:
        def __init__(self, data=None, next=None):
        self.data = data	# data field
        self.next = next	# pointer to the next node
    '''
    def sortedInsert(self, head, node):
        
        current = head 
        if head is None or head.data > node.data:
            node.next = head
            head = node
            return head 

        while current.next and current.next.data < node.data:
            current = current.next 
        
        node.next = current.next
        current.next = node
        return head

    def pop(self, head):
        if head is None:
            return None
        head = head.next 
        return head

    def get_length(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next 
        return count 
        
    def findKthNode(self, head, k):
        # current = head 
        # length = self.get_length(head)
        # for i in range(length - k):
        #     current = current.next

        current = head 
        for i in range(k):
            current = current.next 

        while current:
            current = current.next
            head = head.next
        
        return head.data

    def findKthNodeRecursive(self, head, k):
        if head is None:
            return 0
        count = self.findKthNodeRecursive(head.next, k) + 1
        if count == k:
            print(head.data)
        return count

    def insert_at_index(self, head, node, index):
        temp = head
        for i in range(index - 1):
            temp = temp.next
        node.next = temp.next
        temp.next = node
        return

if __name__ == '__main__':
    keys = [1, 2, 3, 5, 6]
    L = LinkedList()
    L.construct(keys)
    L.print_list(L.head)
    s = Solution()
    node = Node(7)
    head = s.sortedInsert(L.head, node)
    L.print_list(head)
    s.findKthNodeRecursive(head, 3)
    