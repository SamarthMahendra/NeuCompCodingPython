
# belman ford algorithm

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}



def belman_ford(graph, start, end):
    if start == end:
        return 0


    for i in range(len(graph) - 1):
        for node in graph:
            for neighbour, distance in graph[node]:
                if distance + graph[node][0][1] < graph[neighbour][0][1]:
                    graph[neighbour][0] = (node, distance + graph[node][0][1])

    return graph[end][0][1]