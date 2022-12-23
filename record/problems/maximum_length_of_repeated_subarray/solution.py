class Solution:  # 5520 ms, faster than 19.52%
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        # dp[i][j] is the length of Repeated Subarray end with nums1[i] and nums2[j]
        dp = [ [0]*n2 for _ in range(n1) ]
        ans = 0
        for i in range(n1):
            for j in range(n2):
                # here is the base case.
                if i == 0 or j == 0:
                    if nums1[i] == nums2[j]:
                        dp[i][j] = 1 
                else:
                    if nums1[i] == nums2[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                ans = max(dp[i][j], ans )
        return ans


                