# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def find_parent(root):
            if root.left:
                parent[root.left.val] = root
                find_parent(root.left)
            if root.right:
                parent[root.right.val] = root
                find_parent(root.right)
                
        def dfs(i, node, visit=None):
            if not node: return
            if i == k: 
                res.append(node.val)
                return
            if node.left != visit:
                dfs(i+1, node.left, node)
            if node.right != visit:
                dfs(i+1, node.right, node)
            if node.val in parent.keys() and parent[node.val] != visit:
                dfs(i+1, parent[node.val] , node)
                 
                
        parent = dict()
        find_parent(root)
        res = []
        dfs(0, target)
        return res
         
            