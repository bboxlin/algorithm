class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dnums = set(nums)
        ans = 0
        for num in nums:
            curlen = 1 
            if num in dnums:
                dnums.remove(num)
            
            right = num + 1
            while right in dnums:
                dnums.remove(right)
                right += 1
                curlen += 1
                
            left = num - 1
            while left in dnums:
                dnums.remove(left)
                left -= 1
                curlen += 1
                
            ans = max(curlen, ans)
        return ans
            