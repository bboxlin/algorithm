class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #  perhaps overlap occur in:
        #  start <= end >= nextStart <= nextEnd
        #  lower bound = min(start, nextStart)
        #  upper bound = max(end, nextEnd)
        
        #  buf if starts are sorted
        #  start <= end >= nextStart <= nextEnd, where start must <= nextStart
        #  lower bound = start
        #  upper bound = max(end, nextEnd)
        
        intervals.sort(key = lambda x : x[0]) # sort by lower bound 
        res = [intervals[0]]
        for nextStart, nextEnd in intervals[1:]:
            end = res[-1][1]
            if end >= nextStart:
                res[-1][1] = max(end, nextEnd)
            else:
                res.append([nextStart, nextEnd])
        return res
            