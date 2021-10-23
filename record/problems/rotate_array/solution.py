class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseSub(arr, i, j):
            while i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1
                i += 1
        k = k % len(nums)
        nums.reverse()
        reverseSub(nums, 0, k-1)
        reverseSub(nums, k, len(nums)-1)