from collections import OrderedDict
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # extend one unit
        res = [0]*(length+1)
        for start, end, amount in updates:
            res[start] += amount
            res[end+1] -= amount
        for i in range(1, length):
            res[i] += res[i-1]
        return res[:-1]