class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(self.V)]

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def findConnectedComponents(self):
        visited = set()
        cc = []
        for i in range(self.V):
            if i not in visited:
                temp = []
                cc.append(self.explore(temp, visited, self.adj, i))
        return cc

    def explore(self, temp, visited, graph, node):
        visited.add(node)
        temp.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                self.explore(temp, visited, graph, neighbour)

        return temp

        
if __name__ == '__main__':
    V = 5
    graph = Graph(5)
    graph.addEdge(1, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    print(graph.findConnectedComponents())
