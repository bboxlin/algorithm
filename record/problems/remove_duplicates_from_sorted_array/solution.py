class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        i, j = 0, 0
        while j<len(arr):
            if i == 0 or arr[j] != arr[i-1]:
                arr[i] = arr[j]
                i+=1
                j+=1
            else: 
                j+=1
        return i