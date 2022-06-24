import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.words = [] 
        
    def insert(self, product):
        node = self
        for c in product:
            node = node.children[c]   
            if len(node.words) < 3: 
                node.words.append(product)
    
    def search(self, searchWord):
        ans = []
        node = self
        for c in searchWord:
            node = node.children[c]
            ans.append(node.words)
        return ans
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        for product in products:
            root.insert(product)
        return root.search(searchWord)
        
      