class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        q = collections.deque()
        l = 0
        
        for i in range(len(nums)):

            # pop the q head if coming number is larger
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            q.append(i)
            
            if l > q[0]:
                q.popleft()
                
            if(i+1) >= k:
                res.append(nums[q[0]])
                l+=1
        
        return res
                