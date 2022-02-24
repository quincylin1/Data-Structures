def print_list(head):
    list_str = ''
    temp = head
    while temp:
        list_str += str(temp.data) + '->'
        temp = temp.next
    list_str += 'None'
    print(list_str)

class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
	
class Solution:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        return 

    def construct(self, keys):
        for key in keys:
            self.insert_at_end(key)
        return self.head
		
if __name__ == '__main__':
    keys = [1, 2, 3, 4, 5]
    s = Solution()
    head = s.construct(keys)
    print_list(head)