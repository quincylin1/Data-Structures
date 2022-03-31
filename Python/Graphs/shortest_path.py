from collections import defaultdict

def build_graph(edges):
    graph = defaultdict(list)

    for edge in edges:
        v1, v2 = edge[0], edge[1]
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return graph

def shortest_path(graph, start, end):
    explored = []

    queue = [[start]]

    if start == end:
        return start
    
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                print(new_path)
                queue.append(new_path)
                print(queue)

                if neighbour == end:
                    print('Shortest path is ', *new_path)
                    return 

            explored.append(node)
    
    print(f'Path between {start} and {end} does not exist.')
    return


if __name__ == '__main__':
    edges = [
        ["A", "B"], ["A", "E"],
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]

    graph = build_graph(edges)
    shortest_path(graph, 'A', 'D')