class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l,r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]
            if p == k:
                return nums[p]
            elif p > k:
                return quickSelect(l, p-1)
            else:
                return quickSelect(p+1, r)
        k = len(nums)-k
        return quickSelect(0, len(nums)-1)
