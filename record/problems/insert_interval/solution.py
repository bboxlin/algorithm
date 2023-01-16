class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] 
        for i in range(len(intervals)):
            # newInterval to be inserted before i
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            # newInterval to be inserted after i
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            # merge
            else: 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res



