class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        nums.sort()
        lookup = collections.defaultdict(list)
        for i, n in enumerate(nums):
            sum_digit = sum( [int(c) for c in str(n) ] )
            lookup[sum_digit].append(i)

        maxx_summ = -1        
        for sum_digit, indexes in lookup.items():
            if len(indexes) < 2: continue
            maxx_summ = max(maxx_summ, nums[indexes[-1]] + nums[indexes[-2]])   
        return maxx_summ
                    