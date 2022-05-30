class Solution:
    def dailyTemperatures(self, tems: List[int]) -> List[int]:
        res = [0]*len(tems)
        decreStack = []
        for i, tem in enumerate(tems):
            while decreStack and tems[decreStack[-1]] < tem:
                prev_day = decreStack.pop()
                res[prev_day] = i - prev_day 
            decreStack.append(i)
        return res