class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,n in enumerate(nums):
            rem = target - n
            if rem in dic:
                return [i, dic[rem]]
            dic[n] = i
        return [-1, -1]