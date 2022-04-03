class NodeHeap:
    def __init__(self):
        self.nodes = []
        self.heapSize = 0
        self.nodeIndex = dict()  # node->int
        self.distanceMap = dict()  # node->int

    def isEmpty(self):
        return self.heapSize == 0
