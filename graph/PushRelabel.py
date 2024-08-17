class PushRelabel:
    def __init__(self, graph, source, sink):
        self.graph = graph  # Adjacency matrix of capacities
        self.n = len(graph)
        self.source = source
        self.sink = sink
        self.height = [0] * self.n
        self.excess = [0] * self.n
        self.flow = [[0] * self.n for _ in range(self.n)]

    # Initializes  preflow by sending as much flow as possible from the source node to its neighbors.
    def initialize_preflow(self):
        self.height[self.source] = self.n
        for v in range(self.n):
            if self.graph[self.source][v] > 0:
                self.flow[self.source][v] = self.graph[self.source][v]
                self.flow[v][self.source] = -self.flow[self.source][v]
                self.excess[v] = self.graph[self.source][v]
                self.excess[self.source] -= self.graph[self.source][v]

    def push(self, u, v):
        # minimum of the excess at u and the remaining capacity on the edge u->v.
        delta = min(self.excess[u], self.graph[u][v] - self.flow[u][v])
        # Updates the flow in both directions (u->v and v->u) and adjusts the excess flows of u and v.
        self.flow[u][v] += delta
        self.flow[v][u] -= delta
        self.excess[u] -= delta
        self.excess[v] += delta

    def relabel(self, u):
        # minimum height of the neighbors of u to which it can push flow
        min_height = float('Inf')
        for v in range(self.n):
            if self.graph[u][v] - self.flow[u][v] > 0:
                min_height = min(min_height, self.height[v])
        # height of u to one more than this minimum height
        self.height[u] = min_height + 1


    # Discharges a node u by either pushing flow to its neighbors or relabeling it.
    def discharge(self, u):
        while self.excess[u] > 0:
            for v in range(self.n):
                # While there is excess flow at u, it attempts to push flow to a neighbor v.
                if self.graph[u][v] - self.flow[u][v] > 0 and self.height[u] == self.height[v] + 1:
                    self.push(u, v)
                    if self.excess[u] == 0:
                        break
            else:
                # If no push is possible (due to height conditions not being met), the node u is relabeled.
                self.relabel(u)

    # Push-Relabel algorithm using the "relabel-to-front" heuristic.
    def relabel_to_front(self):
        self.initialize_preflow()
        vertices = [i for i in range(self.n) if i != self.source and i != self.sink]
        i = 0
        # Iteratively discharges nodes, relabeling and possibly moving them to the front of the list if their height increases.
        while i < len(vertices):
            u = vertices[i]
            old_height = self.height[u]
            self.discharge(u)
            if self.height[u] > old_height:
                vertices.insert(0, vertices.pop(i))
                i = 0
            else:
                i += 1
        return sum(self.flow[self.source][i] for i in range(self.n))

    def print_residual_network(self):
        print("Residual Network:")
        for u in range(self.n):
            for v in range(self.n):
                if self.graph[u][v] > 0 and self.flow[u][v]>0:  # Only print edges with capacity
                    print(f"{u} -> {v} | capacity: {self.graph[u][v]} | flow: {self.flow[u][v]}")

graph = [
    [0, 16, 13, 0, 0, 0],  # Node 0
    [0, 0, 10, 12, 0, 0],  # Node 1
    [0, 4, 0, 0, 14, 0],   # Node 2
    [0, 0, 9, 0, 0, 20],   # Node 3
    [0, 0, 0, 7, 0, 4],    # Node 4
    [0, 0, 0, 0, 0, 0]     # Node 5
]

source = 0
sink = 5

push_relabel = PushRelabel(graph, source, sink)
max_flow = push_relabel.relabel_to_front()

print(f"Maximum flow: {max_flow}")
push_relabel.print_residual_network()
