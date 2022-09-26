# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS 
        ans = [] 
        if not root: return ans
        q = deque([root])
        while q:
            level_size = len(q)
            curlevelNodes = []
            # 同一个level遍历
            for _ in range(level_size):
                node = q.popleft()
                curlevelNodes.append(node.val)
                
                leftnode = node.left 
                rightnode = node.right 
                if leftnode:
                    q.append(leftnode)
                if rightnode:
                    q.append(rightnode)
            ans.append(curlevelNodes)
        return ans
            
                