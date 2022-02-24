from turtle import left


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def breath_first_traversal(root):
    queue = [root]
    result = []
    while len(queue):
        current = queue.pop(0)
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result 


if __name__ == '__main__':
    '''
            1
           / \
          2   3
         /   / \
        4   5   6
           / \
          7   8
 
    '''
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print(breath_first_traversal(root))
