class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dst):
        node = AdjNode(dst)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dst]
        self.graph[dst] = node

    def print_graph(self):
        for i in range(self.V):
            print(f'Adjacent vertices of vertex {i} are:', end=' ')
            current = self.graph[i]
            while current:
                print(f'--> {current.vertex}', end=' ')
                current = current.next 
            print()


def depthFirstSearch(visited, graph, node):
    if node not in visited:
        visited.add(node)
    
    print('-->', node, end=' ')
    for neighbours in graph[node]:
        depthFirstSearch(visited, graph, neighbours)

def breathFirstSearch(visited, graph, node):
    queue = [node]
    while len(queue):
        current = queue.pop(0)
        visited.add(current)
        print('-->', current, end=' ')
        for neighbours in graph[current]:
            if neighbours not in visited:
                queue.append(neighbours)
        
def hasPath(graph, start, end):
    if start == end:
        return True 

    for neighbour in graph[start]:
        if hasPath(graph, neighbour, end):
            return True
    
    return False

def findConnectedComponents(graph):
    visited = set()
    cc = []

    for node in graph:
        if node not in visited:
            temp = []
            cc.append(exploreFind(temp, visited, graph, node))


    return cc

def exploreFind(temp, visited, graph, node):
    
    visited.add(node)
    temp.append(node)
    
    for neighbour in graph[node]:
        if neighbour not in visited:
            exploreFind(temp, visited, graph, neighbour)
    return temp
    
def countConnectedComponents(graph):
    count = 0
    visited = set()
    for node in graph:
        if exploreCount(visited, graph, node):
            count += 1

    return count 

def exploreCount(visited, graph, node):
    if node in visited:
        return False
    
    visited.add(node)
    for neighbour in graph[node]:
        exploreCount(visited, graph, neighbour)

    return True

    



def DFT(graph, node):
    print('-->', node, end=' ')
    for neighbour in graph[node]:
        DFT(graph, neighbour)

if __name__ == '__main__':
    # graph = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [],
    #     'E': ['F'],
    #     'F': []
    # }

    visited = set()
    # depthFirstSearch(visited, graph, 'A')
    # breathFirstSearch(visited, graph, 'A')
    # print(hasPath(graph, 'D', 'F'))
    # DFT(graph, 'A')

    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    print(countConnectedComponents(graph))
    print(findConnectedComponents(graph))


