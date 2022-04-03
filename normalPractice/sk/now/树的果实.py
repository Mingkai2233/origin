class Node:
    def __init__(self, val):
        self.num = val
        self.val = 0
        self.childs = []


def process(node, dit):
    if node is None:
        return
    for c in node.childs:
        if c.val in dit.keys():
            dit[c.val] += 1
        else:
            dit[c.val] = 1
        process(c, dit)


n, m, c = map(int, input().split())
nodes = [Node(i) for i in range(1, n+1)]
nodes = [None] + nodes
for i in range(1, n):
    a, b , c = map(int, input().split())
    nodes[a].childs.append(nodes[b])
    nodes[b].val = c
query = []
for i in range(m):
    query.append(int(input()))
for i in query:
    dit =dict()
    process(nodes[i], dit)
    res = 0
    for key, val in dit.items():
        res += (key*val)**2
    print(res)
