# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        oddLevelNodes = defaultdict(list)
        def dfs(node, level):
            if not node:return
            if level % 2 != 0:
                oddLevelNodes[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        
        curlevel = 0
        q = deque([root])
        while q:
            level_size = len(q)
            for _ in range(level_size):
                curnode = q.popleft()
                if curlevel in oddLevelNodes.keys():
                    curnode.val = oddLevelNodes[curlevel].pop()
                lnode = curnode.left
                rnode = curnode.right
                if lnode: 
                    q.append(lnode)
                if rnode: 
                    q.append(rnode)
            curlevel += 1
        return root
        
                