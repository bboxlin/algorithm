class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freqCnter = Counter(nums)
        ans = [0, 0]
        for num, freq in freqCnter.items():
            pairs = freq // 2
            ans[0] += pairs
            rem = freq % 2 
            ans[1] += rem
        return ans
                