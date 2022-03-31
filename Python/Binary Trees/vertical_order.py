'''
Given a binary tree, print it vertically:

Example: 
             1
            / \
           /   \
          2     3
         / \   / \
        4   5 6   7
               \   \
                8   9

output: 
4
2
5 1 6
3
3 8
7
9

Idea:

1. Calculate the min and max horizontal distance (hd) of tree w.r.t. root 
2. Iterate over each vertical line with hd from min to max 
3. For each vertical line, print node which lines on the line
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

def findMinMax(node, min, max, hd):
    if node is None:
        return 

    if hd < min[0]:
        min[0] = hd
    
    if hd > max[0]:
        max[0] = hd

    findMinMax(node.left, min, max, hd - 1)
    findMinMax(node.right, min, max, hd + 1)

def printVerticalLine(node, line_no, hd):
    if node is None:
        return 

    if hd == line_no:
        print(node.data, end=" ")
    
    printVerticalLine(node.left, line_no, hd - 1)
    printVerticalLine(node.right, line_no, hd + 1)

def verticalOrder(root):
    min = [0]
    max = [0]

    findMinMax(root, min, max, hd=0)

    for line_no in range(min[0], max[0] + 1):
        printVerticalLine(root, line_no, hd=0)
        print()


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    verticalOrder(root)