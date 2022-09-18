class Node:
    def __init__(self):
        self.children = {}
        self.cnt = 0
        
class Trie:
    def __init__(self):
        self.trie = Node()
        
    def insert(self, word):
        node = self.trie
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
            node.cnt += 1
            
    def count(self, word):
        node = self.trie
        ans = 0
        for ch in word:
            ans += node.children[ch].cnt
            node = node.children[ch]
        return ans

class Solution:
    def sumPrefixScores(self, A: List[str]) -> List[int]:
        trie = Trie()

        for a in A:
            trie.insert(a)

        return [trie.count(a) for a in A]
        
        