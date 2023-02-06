class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for j in range( len(nums)//2, len(nums)):
            ans.append(nums[j - len(nums)//2])
            ans.append(nums[j])
        return ans
