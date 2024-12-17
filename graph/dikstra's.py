from graph.PushRelabel import graph

# dikstra's algorithm


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

nodes = set(graph.keys())

def dijkstras(graph, start):
    import heapq
    pq = []
    heapq.heappush(pq, (0, start))

    distances = {
        node : float('inf') for node in nodes
    }
    distances[start] = 0
    while pq:
        cur_distance, cur_node = heapq.heappop(pq)

        if cur_distance > distances[cur_node]:
            continue

        for neighbour, distance in graph[cur_node]:
            d = cur_distance + distance
            if d < distances[neighbour]:
                distances[neighbour] = d
                heapq.heappush(pq, (d, neighbour))

    return distances

print(dijkstras(graph, 'A'))
