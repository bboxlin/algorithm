class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0
        for num in freq.keys():
            if k == 0:
                ans += 1 if freq[num] > 1 else 0 
            else:
                ans += 1 if num + k in freq.keys() else 0 
        return ans 