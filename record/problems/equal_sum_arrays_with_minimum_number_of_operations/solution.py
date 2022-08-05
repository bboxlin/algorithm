class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum2 == sum1:
            return 0
        if sum2 > sum1:
            return self.minOperations(nums2, nums1)
        
        nums1.sort()
        nums2.sort()

        l, r = len(nums1)-1, 0
        diff = sum1 - sum2
 
        cnt = 0
        
        while diff > 0:
            if l < 0 and r >= len(nums2):
                return -1
            elif l < 0:
                diff -= 6 - nums2[r]
                r += 1
            elif r >= len(nums2):
                diff -= nums1[l] - 1
                l -= 1
            elif nums1[l] - 1 > 6 - nums2[r]:
                diff -= nums1[l] - 1
                l -= 1
            else:
                diff -= 6 - nums2[r]
                r += 1
            cnt += 1
        return cnt