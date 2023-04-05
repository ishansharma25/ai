from collections import deque

class Graph:
    def _init_(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def getNeighbours(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]

    def a_star_algorithm(self, startNode, goalNode):
        open_list = [startNode]
        closed_list = []
        g = {}
        g[startNode] = 0
        parents = {}
        parents[startNode] = startNode

        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print("Path doesnot exist")
                return None

            if n == goalNode:
                path = []

                while (parents[n] != n):
                    path.insert(0, n)
                    n = parents[n]
                path.insert(0, startNode)

                print("Path is: " + str(path))
                return path

            for (m, weight) in self.getNeighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.append(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove
                            open_list.add(m)
            open_list.remove
            closed_list.append

        print("Path does not exist")
        return None


adjacency_list = {'A': [('B', 1), ('C', 3), ('D', 7)],'B': [('D', 5)],'C': [('D', 12)]}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')