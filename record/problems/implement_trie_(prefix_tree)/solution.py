"""
For Node Instance with attribute 

- child (edge)
- is_end (leaf)
"""
class Node:
    def __init__(self):
        self.child = {}
        self.is_end = False
        
"""
Trie structure that holds collection of Node.
"""
class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        # cur pointer traverse trie from root
        cur = self.root
        for c in word:
            if not c in cur.child:
                # set current node edge in a weight of character to a new node
                cur.child[c] = Node()
            # traverse to the end
            cur = cur.child[c]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.child:
                return False
            cur = cur.child[c]
        # see if can reach to leaf
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for p in prefix:
            if p not in cur.child:
                return False
            cur = cur.child[p]
        return True
