class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reversing(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        n = len(nums)
        k = k % n
        reversing(nums, 0, n-1)
        reversing(nums, 0, k-1)
        reversing(nums, k, n-1)

        
        # [1,2,3,4,5,6,7]
        # [7,6,5,4,3,2,1]


