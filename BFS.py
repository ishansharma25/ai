from collections import defaultdict
class Graph:

    def __init__(self):

        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def bfs(self,s):

        visitted=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visitted[s]=True

        while queue:

            s=queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visitted[i]==False:
                    queue.append(i)
                    visitted[i]=True


g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.bfs(2)