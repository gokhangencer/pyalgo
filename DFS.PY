def dfs_all_paths(graph, start, end):
    stack = [(start, [start], 0)]
    paths = []

    while stack:
        (node, path, cost) = stack.pop()

        if node == end:
            paths.append((path, cost))
        else:
            for next_node, next_cost in graph[node]:
                if next_node not in path:
                    stack.append(
                        (next_node, path + [next_node], cost + next_cost))

    return paths


graph = {
    'A': [('B', 3), ('D', 2)],
    'B': [('A', 3), ('C', 5), ('E', 4)],
    'C': [('B', 5), ('E', 6), ('F', 2)],
    'D': [('A', 2), ('E', 1)],
    'E': [('B', 4), ('C', 6), ('D', 1), ('F', 8), ('G', 7)],
    'F': [('C', 2), ('E', 8), ('G', 1)],
    'G': [('E', 7), ('F', 1)]
}

all_paths = dfs_all_paths(graph, 'A', 'G')

for path, cost in all_paths:
    print("Path:", path)
    print("Cost:", cost)
