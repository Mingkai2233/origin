import queue
from graphBase import *
import queue
import heapq
import sys


def bfs(v: Vertex):  # 广度优先搜索
    if v is None:
        return
    vistedV = set()  # 已经进入过队列的顶点
    q = queue.Queue(10)  # 队列,用于进行顶点的访问
    q.put(v)
    vistedV.add(v)
    while not q.empty():
        v = q.get()
        print(v.value)
        for i in v.nexts:
            if i not in vistedV:
                q.put(i)
                vistedV.add(i)


def dfs(v: Vertex):
    if v is None:
        return
    vistedV = {v}
    stack = [v]
    print(v.value)
    while len(stack) > 0:  # 栈中从栈低开始存储的是访问的顺序
        cur = stack.pop()
        for i in cur.nexts:
            if i not in vistedV:
                stack.append(cur)
                stack.append(i)
                vistedV.add(i)
                print(i.value)
                break


def buildTheGraph(matrix: list):  # 有向图, matrix是一个二维数组, 第一个值为边的权重, 第二个值为起始点编号, 第三个为终点编号
    lgraph = Graph()
    for i in matrix:
        edgeWeight = i[0]
        begin = i[1]
        end = i[2]
        # 根据不同情况获得相应的顶点
        if begin not in lgraph.vertexs.keys():
            beginV = Vertex(begin, [], [])
            lgraph.vertexs[begin] = beginV
        else:
            beginV = lgraph.vertexs[begin]
        if end not in lgraph.vertexs.keys():
            endV = Vertex(end, [], [])
            lgraph.edges.add(edge)
        else:
            endV = lgraph.vertexs[end]
        # 创建边
        edge = Edge(edgeWeight, beginV, endV)
        # 修改图中的数据
        beginV.edges.append(edge)
        beginV.nexts.append(endV)
        beginV.outdegree += 1
        endV.indegree += 1
        lgraph.vertexs[end] = endV
    return lgraph


# 构造无向图
def buildUndigraph(matrix: list) -> Graph:
    lgraph = Graph()
    for i in matrix:
        weight = i[0]
        vertex1 = i[1]  # 顶点编号
        vertex2 = i[2]
        # 根据顶点编号来获得对应顶点对象
        if vertex1 not in lgraph.vertexs.keys():  # 判断当前顶点是否已经被创建
            vertex1 = Vertex(vertex1, [], [])
            lgraph.vertexs[vertex1.value] = vertex1
        else:
            vertex1 = lgraph.vertexs[vertex1]
        if vertex2 not in lgraph.vertexs.keys():
            vertex2 = Vertex(vertex2, [], [])
            lgraph.vertexs[vertex2.value] = vertex2
        else:
            vertex2 = lgraph.vertexs[vertex2]
        # 创建边对象
        edge1 = Edge(weight, vertex1, vertex2)
        edge2 = Edge(weight, vertex2, vertex1)
        lgraph.edges.add(edge1)
        lgraph.edges.add(edge2)
        vertex1.edges.append(edge1)
        vertex2.edges.append(edge2)
        vertex1.nexts.append(vertex2)
        vertex2.nexts.append(vertex1)
        vertex1.indegree += 1
        vertex1.outdegree += 1
        vertex2.indegree += 1
        vertex2.outdegree += 1
    return lgraph


# 拓扑排序算法,没有使用优先级队列
def toplogySort(graph: Graph):
    vertexs = [v for v in graph.vertexs.values()]  # 会改变原图中的数据!!!!!!
    result = []
    vertexs.sort(key=lambda x: x.indegree, reverse=True)
    while len(vertexs) > 0:
        v = vertexs.pop()  # 弹出当前入度为0的顶点进行处理
        result.append(v.value)
        for i in v.nexts:  # 更新其他顶点的入度
            i.indegree -= 1
        vertexs.sort(key=lambda x: x.indegree, reverse=True)
    print(result)


def krusal(lgraph: Graph):
    edges = list(lgraph.edges)
    edges.sort(key=lambda x: x.weight, reverse=True)
    edgesSelected = []
    mySets = dict()
    for v in lgraph.vertexs.values():  # 为每个顶点建立一个集合,为接下来的集合的判断和合并做准备
        mySets[v] = {v}
    while len(edges) > 0:
        e = edges.pop()  # 选择一个当前wight最小的未被处理过的边
        if not (mySets[e.begin] is mySets[e.end]):  # 判断该边加入是否会成环
            mySets[e.begin] = mySets[e.begin] | mySets[e.end]
            for i in mySets[e.begin]:
                mySets[i] = mySets[e.begin]
            edgesSelected.append(e)
    for e in edgesSelected:
        print(e.begin.value, "->", e.end.value, " ", e.weight)


def prim(graph: Graph):
    pq = queue.PriorityQueue()
    vertexs = set()  # 记录当前生成树中的顶点
    edges = []  # 记录生成树中的边
    for v in graph.vertexs.values():  # 随机选一个顶点
        if v not in vertexs:
            vertexs.add(v)
            for e in v.edges:  # 将该顶点连接的边全部放进优先级队列, 以v为起点的边
                pq.put(e)
            while not pq.empty():
                e = pq.get()  # 获得当前解锁边中权值最小的边
                otherV = e.end
                if otherV not in vertexs:  # 判断当前边的另一端点是否被选中(即是否会形成环)
                    edges.append(e)
                    vertexs.add(otherV)
                    for e in otherV.edges:  # 将与新加入顶点相连的边加入到优先级队列中
                        pq.put(e)
    for e in edges:
        print(e.begin.value, "->", e.end.value, e.weight)


# 寻找指定顶点到全图其他顶点的最短路径
def Dijkstra(vertex: Vertex):
    vertexSelected = set()
    distanceMap = {vertex: 0}  # 不存在的项表示原点到该点的距离为无穷
    v1 = findTheMinAndUnselectedVertex(distanceMap, vertexSelected)
    while v1 is not None:
        for e in v1.edges:
            v2 = e.end
            if v2 not in distanceMap.keys():
                distanceMap[v2] = distanceMap[v1] + e.weight
            else:
                distanceMap[v2] = min(distanceMap[v2], distanceMap[v1]+e.weight)
        vertexSelected.add(v1)
        v1 = findTheMinAndUnselectedVertex(distanceMap, vertexSelected)
    for key, value in distanceMap.items():
        print(vertex.value, "->", key.value, value)


# 辅助函数, 可以用堆进行优化, p10
def findTheMinAndUnselectedVertex(distanceMap: dict, vertexSelected: set):
    minV = None
    minD = sys.maxsize
    for key, value in distanceMap.items():
        if key not in vertexSelected and value < minD:
            minV = key
            minD = value
    return minV


if __name__ == '__main__':
    # 有向图
    matrix = [[2, 1, 2],
              [3, 1, 3],
              [2, 2, 4],
              [4, 2, 5],
              [1, 3, 7],
              [7, 3, 6],
              [8, 7, 6],
              [6, 5, 3]]
    udg = buildUndigraph(matrix)
    Dijkstra(udg.vertexs[1])

