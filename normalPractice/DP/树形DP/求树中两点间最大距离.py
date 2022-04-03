from DP.treeNode import *


class Info:
    def __init__(self, heigth, length):
        self.heigth = heigth
        self.length = length


def info(node: Node):
    if node is None:
        return Info(0, 0)
    i1 = info(node.leftC)
    i2 = info(node.rightC)
    heigth = max(i1.heigth, i2.heigth) + 1
    length = max(i1.heigth+i2.heigth+1, i1.length, i2.length)
    return Info(heigth, length)


nodes = [None]
for i in range(1, 8):
    nodes.append(Node(i))
nodes[1].leftC = nodes[2]
nodes[1].rightC = nodes[3]
nodes[2].leftC = nodes[4]
nodes[2].rightC = nodes[5]
nodes[3].rightC = nodes[6]
nodes[6].leftC = nodes[7]
root = nodes[1]
i = info(root)
print(i.heigth, i.length)