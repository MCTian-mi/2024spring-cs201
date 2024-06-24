class Vertex:
    _ID = 0
    id:int
    weight:int
    connectedTo:dict
    connectCount:int
    isDirty:bool
    def __init__(self, id, weight) -> None:
        self.id = id
        self.weight = weight
        self.connectCount = 0
        self.connectedTo = {}
        self.isDirty = False
    
    def connectTo(self, other, weight=1):
        self.connectedTo[other] = weight
        self.connectCount += 1
        other.connectedTo[self] = weight
        other.connectCount += 1
        
    def markDirty(self):
        self.isDirty =True
    
class Graph:
    vertexNumber:int
    id_dict:dict
    def __init__(self):
        self.vertexNumber = 0
        self.id_dict = {}
        
    def addVertex(self, vertex:Vertex):
        self.id_dict[vertex.id] = vertex
        self.vertexNumber += 1
        
    def addVertexSafe(self, vertex:Vertex):
        if not vertex.id in self.id_dict:
            self.addVertex(vertex)
            
    def addEdge(self, v1:Vertex, v2:Vertex, w=1):
            v1.connectTo(v2, w)
            
    def addEdgeSafe(self, v1:Vertex, v2:Vertex):
        self.addVertexSafe(v1); self.addVertexSafe(v2)
        self.addEdge(v1, v2)
    
    def createEdgeSafe(self, n1:int, n2:int):
        v1 = self.id_dict[n1]
        v2 = self.id_dict[n2]
        self.addEdge(v1, v2)
        
    def _adjacencyMatrix(self):
        outL = [[0] * self.vertexNumber for _ in range(self.vertexNumber)]
        for id1 in self.id_dict:
            vertex = self.id_dict[id1]
            for other in vertex.connectedTo:
                id2 = other.id
                outL[id1][id2] = -vertex.connectedTo[other]
        return outL
    
    def _laplaceMatrix(self):
        outL = self._adjacencyMatrix()
        for id in self.id_dict:
            outL[id][id] += self.id_dict[id].connectCount
        return outL
    
    def __str__(self):
        l = self._laplaceMatrix()
        return '\n'.join([' '.join([str(x) for x in _]) for _ in l])
    
def BFSVertexParser(vertex:Vertex):
    if vertex.isDirty: return 0
    vertex.markDirty()
    ans = vertex.weight
    for conneted in vertex.connectedTo:
        ans += BFSVertexParser(conneted)
    return ans

def Max(graph:Graph):
    ans = 0
    for vertex in graph.id_dict.values():
        if not vertex.isDirty:
            ans = max(ans, BFSVertexParser(vertex))
    return ans
    
n, m = map(int, input().split())
myGraph =  Graph()
lw = list(map(int, input().split()))
for i in range(n):
    myGraph.addVertex(Vertex(i, lw[i]))
for _ in range(m):
    n1, n2 = map(int, input().split())
    myGraph.createEdgeSafe(n1, n2)
print(Max(myGraph))