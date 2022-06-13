# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    node_count = 0
    max_position = 0

    def isCompleteTree(self, root):
        self.isCompleteTreeHelper(root, 1)
        return self.max_position == self.node_count

    def isCompleteTreeHelper(self, root, position):
        if root is None:
            return
        self.node_count += 1
        self.max_position = max(self.max_position, position)
        self.isCompleteTreeHelper(root.left, 2 * position)
        self.isCompleteTreeHelper(root.right, 2 * position + 1)

class Solution2:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        isEnd = False
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                isEnd = True
            else:
                if isEnd: return False
                q.append(node.left )
                q.append(node.right)
        return True
                
                
class Solution1:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def findLastNode(root):
            lastnode = root
            q = deque([root])
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    node = q.popleft()
                    lastnode = node
                    leftnode = node.left 
                    rightnode = node.right 
                    if leftnode:
                        q.append(leftnode)
                    if rightnode:
                        q.append(rightnode)
            return lastnode
        
        lastnode = findLastNode(root)
        q = deque([root])
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.popleft() 
                if node == lastnode: # Complete = before lastnode, not encounter any None
                    return True
                if not node:        
                    return False
                leftnode = node.left 
                rightnode = node.right 
                q.append(leftnode)
                q.append(rightnode)
        return True
                