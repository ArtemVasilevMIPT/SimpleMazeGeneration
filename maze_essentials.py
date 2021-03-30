import random
import time
from utility import DSU, manhattanHeuristic, findNextNode
import queue


# Maze class
class Maze:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.maze = {}
        self.start = (0, 0)
        self.end = (height - 1, width - 1)
        self.seed = time.time()
        for row in range(height):
            for col in range(width):
                self.maze[(row, col)] = []

    def getMaze(self):
        buff = [[1 for j in range(self.w * 2)] for i in range(self.h * 2)]
        for (key, elem) in self.maze.items():
            buff[2 * key[0] + 1][2 * key[1] + 1] = 0
            for point in elem:
                offX = point[0] - key[0]
                offY = point[1] - key[1]
                buff[2 * key[0] + 1 + offX][2 * key[1] + 1 + offY] = 0
        return buff

    def print(self):
        b = self.getMaze()
        for i in b:
            for j in i:
                print(j, sep='', end='')
            print()

    def printRaw(self):
        print(self.maze)

    def reset(self, filler=0):
        for row in range(self.h):
            for col in range(self.w):
                self.maze[(row, col)] = []

    def generateDFS(self):
        random.seed(self.seed)
        self.reset()
        self.start = (0, 0)
        stack = []
        # Create "used" array
        # 0 - not used
        # 1 - used
        used = [[0 for j in range(self.w)] for i in range(self.h)]

        used[self.start[0]][self.start[1]] = 1
        numUsed = self.w * self.h
        current = self.start

        while numUsed > 0 or len(stack) != 0:
            # Add neighbours
            neighbours = []
            if current[0] > 0 and used[current[0] - 1][current[1]] == 0:
                neighbours += [(current[0] - 1, current[1])]
            if current[0] < self.h - 1 and used[current[0] + 1][current[1]] == 0:
                neighbours += [(current[0] + 1, current[1])]
            if current[1] > 0 and used[current[0]][current[1] - 1] == 0:
                neighbours += [(current[0], current[1] - 1)]
            if current[1] < self.w - 1 and used[current[0]][current[1] + 1] == 0:
                neighbours += [(current[0], current[1] + 1)]
            if len(neighbours) != 0:
                random.shuffle(neighbours)
                stack.insert(0, current)
                self.maze[current] += [neighbours[0]]
                self.maze[neighbours[0]] += [current]
                current = neighbours[0]
                used[current[0]][current[1]] = 1
            elif len(stack) != 0:
                current = stack[0]
                stack.pop(0)
            else:
                for i in range(self.h):
                    for j in range(self.w):
                        if used[i][j] == 0:
                            current = (i, j)
                            used[i][j] = 1
                            i = self.h
                            j = self.w
            numUsed -= 1

    def generateKruskal(self):
        random.seed(self.seed)
        self.reset()
        nodes = [(i, j) for j in range(self.w) for i in range(self.h)]
        neighbors = lambda n: [(n[0] + dx, n[1] + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
                               if n[0] + dx >= 0 and n[0] + dx < self.h and n[1] + dy >= 0 and n[1] + dy < self.w]
        edges = [(node, neigh) for node in nodes for neigh in neighbors(node)]
        ds = DSU(nodes)
        maze = []
        while len(maze) < len(nodes) - 1:
            edge = edges.pop(random.randint(0, len(edges) - 1))
            if ds.find_set(edge[0]) != ds.find_set(edge[1]):
                ds.union_sets(edge[0], edge[1])
                maze.append(edge)

        for elem in maze:
            self.maze[elem[0]] += [elem[1]]
            self.maze[elem[1]] += [elem[0]]

    def findBFS(self, start, end):
        expandedNodes = [start]
        parents = {start: start}
        visited = set(start)
        visitedNodes = queue.PriorityQueue()
        currentNode = start
        while True:
            if end in visited:
                break
            for x in self.maze[currentNode]:
                if not (x in visited):
                    visited.add(x)
                    parents[x] = currentNode
                    visitedNodes.put((manhattanHeuristic(x, end), x))
            currentNode = visitedNodes.get(0)[1]
            expandedNodes += [currentNode]
        path = []
        node = end
        while node != start:
            path += [node]
            node = parents[node]
        path += [start]
        return path, expandedNodes

    def findAStar(self, start, end):
        expandedNodes = set()
        visitedNodes = {}
        expandedNodes.add(start)
        visited = set(start)
        costFromOrigin = {}
        costFromOrigin[start] = 0
        parents = {start: start}
        currentNode = start
        while True:
            if expandedNodes.__contains__(end):
                break
            for x in self.maze[currentNode]:
                if expandedNodes.__contains__(x):
                    continue
                if not (x in visited):
                    visited.add(x)
                    parents[x] = currentNode
                    costFromOrigin[x] = costFromOrigin[currentNode] + 1
                    cost = costFromOrigin[x] + manhattanHeuristic(x, end)
                    visitedNodes.update({x : cost})
                else:
                    newCost = costFromOrigin[currentNode] + 1
                    if newCost < costFromOrigin[x]:
                        costFromOrigin[x] = newCost
                        parents[x] = currentNode
                        del visitedNodes[x]
                        visitedNodes.update({x: (costFromOrigin[x] + manhattanHeuristic(x, end))})
            currentNode = findNextNode(visitedNodes)
            del visitedNodes[currentNode]
            expandedNodes.add(currentNode)
        path = []
        node = end
        while node != start:
            path += [node]
            node = parents[node]
        path += [start]
        return path, expandedNodes
