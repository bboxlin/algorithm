# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        def bfs(p,q):
            que = collections.deque()
            que.append(p)
            que.append(q)
            while que:
                node1 = que.popleft()
                node2 = que.popleft()

                if node1 == None and node2 == None: continue
                if node1 == None or node2 == None or node1.val != node2.val: return False

                que.append(node1.left)
                que.append(node2.left)

                que.append(node1.right)
                que.append(node2.right)
            return True
        return bfs(p,q)
    
#         def dfs(p,q):
            
#             if p == None and q == None: return True
#             elif p == None or q == None: return False
            
#             if p.val == q.val:
#                 return dfs(p.left, q.left) and dfs(p.right, q.right)
#             else:
#                 return False
            
#         return dfs(p,q)