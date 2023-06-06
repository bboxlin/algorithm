class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        for i in range(2, n):
            if arr[i] - arr[i-1] != arr[i-1] - arr[i-2]:
                return False 
        return True