class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def counter_allzero():
            for v in counter.values():
                if v != 0:
                    return False
            return True
        
        if len(s1) > len(s2): return False
        
        # prepare the counter for s1
        counter = {}
        for c in s1:
            if c not in counter: counter[c] = 1
            else: counter[c] += 1
        
        # check if the first window of s2 is permutation or not
        window_size = len(s1)
        for i in range(window_size):
            c = s2[i]
            if c in counter:
                counter[c] -= 1
        if counter_allzero(): return True
        
        # check for the rest windows
        for i in range(window_size, len(s2)):
            fast = s2[i]
            slow = s2[i-window_size]
            if fast in counter:
                counter[fast] -= 1
            if slow in counter:
                counter[slow] += 1
            if counter_allzero():
                return True
        return False
                
            
            
            