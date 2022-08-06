class Solution:
    # j - i != nums[j] - nums[i]
    # --> j  != nums[j] - nums[i] + i
    # --> j - nums[j] != i - nums[i]
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        totalPairs =  n * (n - 1) // 2
        goodPairs = 0
        dic = defaultdict(int)
        for i in range(n):
            goodPairs += dic[i - nums[i]]
            dic[i - nums[i]] += 1
        return totalPairs - goodPairs