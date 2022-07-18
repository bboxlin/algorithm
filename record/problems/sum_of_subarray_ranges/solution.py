class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
         
        inf = float('inf')
        arr = [-inf] + nums + [-inf] 
        res = 0
       
    
        # min minus
        incre_stack = []
        for i, num in enumerate(arr):
            # incoming num < stack top
            while incre_stack and arr[incre_stack[-1]] > num:
                localMin_idx = incre_stack.pop()
                localMin = arr[localMin_idx] 
                res -= localMin * (i - localMin_idx)* (localMin_idx - incre_stack[-1])
            incre_stack.append(i)
         
         
        # max plus 
        arr = [inf] + nums + [inf] 
        decre_stack = []
        for i, num in enumerate(arr):
            while decre_stack and arr[decre_stack[-1]] < num:
                localMax_idx = decre_stack.pop()
                localMax = arr[localMax_idx]
                res += localMax * (i - localMax_idx) * (localMax_idx - decre_stack[-1])
            decre_stack.append(i)
 
            
        return res