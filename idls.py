from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self, u, v):
        self.graph[u].append(v)
    def dls(self,s,target,max_depth):
        if s==target:
            return True
        if max_depth<=0:
            return False
        for i in self.graph[s]:
            if(self.dls(i,target,max_depth-1)):
                return True
        return False
    def idfs(self,s,target,max_depth):
        for i in range(max_depth):
            if(self.dls(s,target,i)):
                return True
        return False

g = Graph()
g.addedge(0, 1)
g.addedge(0, 2)
g.addedge(1, 2)
g.addedge(2, 0)
g.addedge(2, 3)
g.addedge(3, 3)

if g.idfs(1,3,2)==True:
       print("yes")
else:
       print("no")