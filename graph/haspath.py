from typing import List
from collections import defaultdict



class Graph:

    def __init__(self, n:int, edges: List[List[int]]):
        self.edges = edges
        self.n = n
        self.graph = self._initializeGraph()

    def _initializeGraph(self):
        dict = defaultdict(list)
        for i in self.edges:
            dict[i[0]].append(i[1])
            dict[i[1]].append(i[0])
        return dict

    def hasPath(self, src:int, dest:int, visited=set()):
        if src ==  dest:
            return True
        visited.add(src)
        for neighbour in self.graph[src]:
            if neighbour not in visited:
                return self.hasPath(neighbour, dest, visited)
        return False




# test
obj = Graph(3, [[0, 1], [1, 2], [2, 3]])

print(obj.hasPath(1,3))


