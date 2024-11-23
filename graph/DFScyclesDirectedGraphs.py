from collections import defaultdict


def detect_cycle_dfs(graph):
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:  # If not visited, explore deeper
                if dfs(neighbor):  # Cycle found in deeper call
                    return True
            elif neighbor in rec_stack:  # Back edge detected
                return True

        rec_stack.remove(node)  # Remove from recursion stack after exploring
        return False

    visited = set()
    rec_stack = set()

    # Check every node in the graph
    for node in graph:
        if node not in visited:
            if dfs(node):  # Cycle detected
                return True
    return False


# Example Usage
if __name__ == "__main__":
    # Create a graph as an adjacency list
    graph = defaultdict(list)
    graph[1] = [2]
    graph[2] = [3]
    graph[3] = [4]
    graph[4] = [2]  # Back edge creating a cycle

    # Detect cycle
    if detect_cycle_dfs(graph):
        print("Cycle detected in the graph!")
    else:
        print("No cycle detected in the graph.")
