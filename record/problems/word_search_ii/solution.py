"""
LC 原題
"""

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)
    
    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True
        cur.word = word
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        root = TrieNode()
        
        for word in words:
            root.insert(word)
    
        def dfs(i, j, parent):
            letter = board[i][j]
            node = parent.children[letter]

            if node.isWord:
                ans.append(node.word)
                node.isWord = False
                
            if not node.children:
                parent.children.pop(letter)
                return
            
            board[i][j] = '*'
            for x, y in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] in node.children: 
                    dfs(x, y, node)        
            board[i][j] = letter
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    dfs(i, j, root)                
        return ans


 