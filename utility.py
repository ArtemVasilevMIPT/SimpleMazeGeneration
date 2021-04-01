class DSU:
    parent = {}
    rank = {}

    def __init__(self, sets=()):
        for elem in sets:
            self.parent[elem] = elem
            self.rank[elem] = 0

    def make_set(self, elem):
        self.parent[elem] = elem
        self.rank[elem] = elem

    def find_set(self, a):
        if a == self.parent[a]:
            return a
        self.parent[a] = self.find_set(self.parent[a])
        return self.parent[a]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.rank[a] < self.rank[b]:
                t = a
                a = b
                b = t
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1


def manhattanHeuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def findNextNode(nodes):
    lowestCost = 10**10
    lowestCostNode = None
    for node in nodes:
        if nodes[node] < lowestCost:
            lowestCostNode = node
            lowestCost = nodes[node]
    return lowestCostNode