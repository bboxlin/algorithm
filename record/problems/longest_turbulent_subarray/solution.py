class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, 0
        ans = 1
        if n == 1: return ans
        while r < n:
            while l < n - 1 and arr[l] == arr[l+1]:
                l += 1
            r = max(r, l)
            while r > 0 and r < n - 1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
                r += 1
            ans=max(ans, r - l + 1)
            l = r # 如果[r+1]不符合l从r开始。。。 也有可能从r+1开始如何arr[r] == arr[r+1] 但是这部分line8解决
            r += 1
        return ans
            

