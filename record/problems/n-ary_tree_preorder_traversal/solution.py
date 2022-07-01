"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def __init__(self):
        self.output = []
        
    def dfs(self, node):
        if not node:
            return 
        self.output.append(node.val)
        for nod in node.children:
            self.dfs(nod)
                   
    def preorder(self, root: 'Node') -> List[int]:
        self.dfs(root)
        return self.output
    
     
        
        
        
        
        
        