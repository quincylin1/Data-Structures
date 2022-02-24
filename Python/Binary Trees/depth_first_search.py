from __future__ import print_function
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    '''
        left -> root -> right
    '''

    if root is None:
        return

    inorder(root.left)
    print(str(root.data) + '->', end="")
    inorder(root.right)

def inorderIter(root):
    output = []
    stack = []
    current = root
    while len(stack) or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            output.append(current.data)
            current = current.right
    return output

def preorder(root):
    '''
    root -> left -> right
    '''

    if root is None:
        return 
    
    print(str(root.data) + '->', end='')
    preorder(root.left)
    preorder(root.right)

def preorderIter(root):
    output = []
    stack = []
    
    stack.append(root)
    while len(stack):
        current = stack.pop()
        output.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        
    return output 

def postorder(root):
    '''
    left -> right -> root
    '''
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(str(root.data) + '->', end='')


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

    postorder(root)

