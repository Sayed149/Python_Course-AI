def local_search(graph, start, goal):
    path = [start]
    visited = set()

    while path:
        current = path[-1]

        if current == goal:
            return path

        visited.add(current)

        next_state = None

        for neighbor in graph[current]:
            if neighbor not in visited:
                next_state = neighbor
                break

        if next_state is not None:
            path.append(next_state)
        else:
            path.pop()

    return None


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['H'],
    'H': []
}

start = 'A'
goal = 'H'

result = local_search(graph, start, goal)

if result:
    print("Path found:")
    print(" -> ".join(result))
else:
    print("No path found")