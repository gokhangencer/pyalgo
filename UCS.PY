# https://www.youtube.com/watch?v=dRMvK76xQJI

import heapq
graph = {
    'A': [('B', 3), ('D', 2)],
    'B': [('A', 3), ('C', 5), ('E', 4)],
    'C': [('B', 5), ('E', 6), ('F', 2)],
    'D': [('A', 2), ('E', 1)],
    'E': [('B', 4), ('C', 6), ('D', 1), ('F', 8), ('G', 7)],
    'F': [('C', 2), ('E', 8), ('G', 1)],
    'G': [('E', 7), ('F', 1)]
}


def ucs(graph, start, goal):
    visited = set()
    heap = [(0, start, [])]
    while heap:
        (cost, current_node, path) = heapq.heappop(heap)
        if current_node not in visited:
            visited.add(current_node)
            path = path + [current_node]
            if current_node == goal:
                return (path, cost)
            for neighbor, c in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + c, neighbor, path))
    return None


start_node = 'A'
goal_node = 'G'
result = ucs(graph, start_node, goal_node)

if result is None:
    print("There is no path from {} to {}".format(start_node, goal_node))
else:
    path, cost = result
    print("The shortest path from {} to {} is: {}".format(
        start_node, goal_node, path))
    print("The cost of the shortest path from {} to {} is: {}".format(
        start_node, goal_node, cost))

    # Tüm yolların yazdırılması
    all_paths = []
    heap = [(0, start_node, [])]
    while heap:
        (cost, current_node, path) = heapq.heappop(heap)
        path = path + [current_node]
        if current_node == goal_node:
            all_paths.append((path, cost))
        for neighbor, c in graph[current_node]:
            if neighbor not in path:
                heapq.heappush(heap, (cost + c, neighbor, path))
    print("All paths from {} to {} are:".format(start_node, goal_node))
    for path, cost in all_paths:
        print("Path: {}, Cost: {}".format(path, cost))
