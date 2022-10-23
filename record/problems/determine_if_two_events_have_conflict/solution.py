class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        times = [event1,event2]
        times.sort()
        if times[1][0] <= times[0][1]:
            return True
        return False