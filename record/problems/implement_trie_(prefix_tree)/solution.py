class Node:
    def __init__(self):
        self.children = {} 
        self.isEnd = False 

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curnode = self.root 
        for c in word:
            if c not in curnode.children.keys():
                curnode.children[c] = Node() 
            curnode = curnode.children[c]
        curnode.isEnd = True

    def search(self, word: str) -> bool:
        curnode = self.root 
        for c in word:
            if c not in curnode.children.keys():
                return False 
            curnode = curnode.children[c]
        return curnode.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curnode = self.root 
        for c in prefix:
            if c not in curnode.children.keys():
                return False 
            curnode = curnode.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)