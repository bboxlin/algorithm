# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        def dfs(node):
            if not node:
                return [] 
            if not node.left and not node.right:
                return [1]
            leftdistances = dfs(node.left)
            rightdistances = dfs(node.right)
            
            for leftdis in leftdistances:
                for rightdis in rightdistances:
                    if leftdis + rightdis <= distance:
                        self.cnt += 1
                        
            return [d + 1 for d in leftdistances + rightdistances if d + 1 < distance]
        
        self.cnt = 0
        dfs(root)
        return self.cnt
        
        
        
class Solution1:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        adjList=defaultdict(list)
        leaves=[]
        ct=0
        
        #[undirected graph two way using parent in postorder style]
        def dfs(node, parent):
            if node:
                if not node.left and not node.right:
                    leaves.append(node)
                adjList[node].append(parent)
                adjList[parent].append(node)
                dfs(node.left,node)
                dfs(node.right,node)
        
        #[construct graph and get leaves]
        dfs(root, None)
        
        #bfs from each leaf
        for leaf in leaves:
            q=deque([(leaf,0)] )
            seen=set()
            while q:
                curr,dist = q.popleft()
                seen.add(curr)
                if dist>distance:
                    break                
                for nbr in adjList[curr]:
                    if nbr and nbr not in seen:
                        if nbr in leaves and dist+1<=distance:
                            ct+=1
                        q.append((nbr,dist+1))
        
        return ct//2
    
    