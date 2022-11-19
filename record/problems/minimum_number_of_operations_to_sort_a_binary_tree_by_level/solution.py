# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        cnt = 0
 
        while q:
            arr = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                arr.append(node.val)
            
            idxmap = { v:i for i, v in enumerate(sorted(arr))}
            for i in range(len(arr)):
                # if current idx is not at correctidx and
                while idxmap[arr[i]] != i:
                    pos = idxmap[arr[i]]
                    # swap arr[i] to the correct position
                    arr[i], arr[pos] = arr[pos], arr[i]
                    cnt += 1
                
        return cnt
 
    # [7,6,8,5]
    #  8.  7 