class Graph:
    def __init__(self):
        self.vertexs = dict()  # 编号:点vertex对象 键值对
        self.edges = set()


class Vertex:
    def __init__(self, value: int, nexts: list, edges: list, indegree=0, outdegree=0):
        self.value = value  # 点上所存储的数字, int
        self.nexts = nexts  # 与该顶点邻接的点,obj
        self.edges = edges  # 该顶点发射出去的边,obj
        self.indegree = indegree  # 入度, int
        self.outdegree = outdegree  # 出度, int


class Edge:
    def __init__(self, weight: int, begin: Vertex, end: Vertex):
        self.weight = weight  # 边的权重 int
        self.begin = begin  # 开始顶点, obj
        self.end = end  # 结束顶点, obj

    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        else:
            return False

