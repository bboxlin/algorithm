class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # arr = sorted(nums)
        # i, j = 0, len(arr) - 1
        # idx = 0
        # while i <= j:
        #     # even, should use i
        #     if idx % 2 == 0:
        #         nums[idx] = arr[i]
        #         i += 1
        #     # odd, should use j
        #     else:
        #         nums[idx] = arr[j]
        #         j -= 1
        #     idx += 1
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop() 
        for i in range(0, len(nums), 2): nums[i] = arr.pop()

       
        # x0 <= x1 >= x2 <= x3 >= x4
        # even  odd.  even. odd 
        # even <= odd
        # 1 2 3 4 5 6 
        #.i.i     j
        # 1 6 2 5 3 4

        # 3 5 6 6 6 8
        # 
        # i         j

        