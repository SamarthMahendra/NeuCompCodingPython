def has_cycle_connected(graph):
    visited = set()
    # Starting DFS from the first vertex in the graph
    return dfs(next(iter(graph)), visited, graph, None)

def dfs(vertex, visited, stack, graph, parent):
    visited.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            if dfs(neighbor, visited, graph, vertex):
                return True
        elif neighbor != parent:
            return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
}
print(has_cycle_connected(graph))
# Output: True