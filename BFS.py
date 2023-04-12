from queue import Queue

graph = {
    'A': [('B', 3), ('D', 2)],
    'B': [('A', 3), ('C', 5), ('E', 4)],
    'C': [('B', 5), ('E', 6), ('F', 2)],
    'D': [('A', 2), ('E', 1)],
    'E': [('B', 4), ('C', 6), ('D', 1), ('F', 8), ('G', 7)],
    'F': [('C', 2), ('E', 8), ('G', 1)],
    'G': [('E', 7), ('F', 1)]
}


def bfs_paths(graph, start, goal):
    queue = [(start, [start], 0)]
    all_paths = []
    while queue:
        (node, path, cost) = queue.pop(0)
        for neighbor, weight in graph[node]:
            if neighbor not in path:
                if neighbor == goal:
                    all_paths.append((path + [neighbor], cost + weight))
                else:
                    queue.append((neighbor, path + [neighbor], cost + weight))
    return all_paths


all_paths = bfs_paths(graph, 'A', 'G')
for path, cost in all_paths:
    print(path, cost)
