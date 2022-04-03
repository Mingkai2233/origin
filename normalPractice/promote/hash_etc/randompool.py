import random
class RandomPool:
    def __init__(self):
        self.keyIndexMap = dict()
        self.indexKeyMap = []
        self.size = 0

    def insert(self, key):
        self.keyIndexMap[key] = self.size
        self.indexKeyMap.append(key)
        self.size += 1

    def delete(self, key):  # 为避免删除元素后indexKeyMap中出现间隙,将结尾的元素填到删除元素的位置,并更改keyIndexMap中的值
        if key in self.keyIndexMap.keys():
            index = self.keyIndexMap[key]
            del self.keyIndexMap[key]
            self.size -= 1
            self.indexKeyMap[index] = self.indexKeyMap[self.size]
            self.keyIndexMap[self.indexKeyMap[self.size]] = index

    def randomGet(self):
        index = random.randint(0, self.size-1)
        return self.indexKeyMap[index]


if __name__ == '__main__':
    rp = RandomPool()
    rp.insert('zhang')
    rp.insert('ming')
    rp.insert('kai')
    for i in range(10):
        print(rp.randomGet())
    rp.delete('zhang')
    for i in range(10):
        print(rp.randomGet())