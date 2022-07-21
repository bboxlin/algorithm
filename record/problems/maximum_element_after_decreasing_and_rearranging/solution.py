class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr = sorted(arr)
        n = len(arr)
        for i in range(n):
            if i == 0:arr[i] =1
            else:
                if arr[i] - arr[i-1] > 1:
                    arr[i] = arr[i-1] + 1
        return arr[-1]