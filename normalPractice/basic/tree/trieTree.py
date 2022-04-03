class TrieNode:
    def __init__(self):
        self.passby = 0
        self.end = 0
        self.nexts = [None for i in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):  # 将单词插入前缀树
        if word is None:
            return
        chars = list(word)  # 先将字符串转为字符列表
        node = self.root
        for c in chars:
            index = ord(c) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node.passby += 1
            node = node.nexts[index]
        node.passby += 1
        node.end += 1

    def search(self, word):
        if word is None:
            return False
        chars = list(word)
        node = self.root
        for c in chars:
            index = ord(c) - ord('a')
            if node.nexts[index] is None:
                return False
            node = node.nexts[index]
        if node.end > 0:  # 与找前缀的区别在这里
            return True
        return False

    def startWith(self, word):
        chars = list(word)
        node = self.root
        for c in chars:
            index = ord(c) - ord('a')
            if node.nexts[index] is None:
                return False
            node = node.nexts[index]
        return True

    def delete(self, word):
        if not self.search(word):
            return False
        chars = list(word)
        node = self.root
        node.passby -= 1
        for c in chars:
            index = ord(c) - ord('a')
            node.nexts[index].passby -= 1
            tmp = node.nexts[index]
            if node.nexts[index].passby <= 0:
                node.nexts[index] = None
            node = tmp
        node.end -= 1


if __name__ == "__main__":
    trie = Trie()
    words = ['apple', 'banana', 'cat', 'father']
    for w in words:
        trie.insert(w)

    print(trie.search('apple'))
    trie.delete('apple')
    print(trie.search('apple'))
    trie.startWith('app')
