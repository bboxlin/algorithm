class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        distinct = set(arr)
        new_arr = sorted(list(distinct))
        for i in range(len(new_arr)):
            arr[i] = new_arr[i]
        return len(distinct)