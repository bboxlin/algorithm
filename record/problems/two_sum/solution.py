class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            rem = target - num 
            if rem in dic.keys():
                return [dic[rem], i]
            dic[num] = i
        return [-1,-1]
    