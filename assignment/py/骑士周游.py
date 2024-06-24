def genLegalMoves(x, y, bdSize):
    newMove = []
    # 马走日8个格子
    moveOffsets = [
        (-1, -2), (-1, 2), (-2, -1), (-2, 1),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    for i in moveOffsets:
        newX = x+i[0]
        newY = y+i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMove.append((newX, newY))
    return newMove

# 确保不会走出棋盘
def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1].bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, col, bdSize):
    return row*bdSize+col

def knightTour(n, path, u, limit):
    """
    n:层次； 
    path:路径； 
    u:当前顶点；
    limit:搜索总深度
    """
    u.setColor('gray')
    # 当前点加入路径
    path.append(u)
    if n < limit:
        # 对所有合法移动逐一深入
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white': # 选择未经过的顶点深入
                done = knightTour(n+1, path, nbrList[i], limit) # 层次+1，递归深入
            i += 1
        # 都无法完成总深度，回溯，试本层下一个顶点
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done