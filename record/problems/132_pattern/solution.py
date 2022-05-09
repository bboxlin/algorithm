class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        curmin = nums[0]
        stack = []    
        for num in nums[1:]:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num < stack[-1][0] and num > stack[-1][1]:
                return True
            stack.append((num, curmin))
            curmin = min(num, curmin)
        return False
                
            