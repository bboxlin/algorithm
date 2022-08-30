class Solution:
    def numSteps(self, s: str) -> int:
        
        # check if its one
        def isOne(q):
            return len(q) == 1 and q[0] == '1'
        
        def isOdd(q):
            return q[-1] == '1'
        
        def addOne(q):
            i = len(q) -1 
            while i >= 0:
                if q[i] == '0':
                    break
                else:
                    q[i] = '0'
                i -= 1
            # encounter a 0 or carry one
            if i >= 0:
                q[i] = '1'
            else:
                q.appendleft('1')
        
        ans = 0
        q = deque([c for c in s])
        while isOne(q) == False:
            if isOdd(q):
                addOne(q)
            else:
                q.pop()  # basically shift left one 1 bit = divide by 2
            ans += 1
        return ans
                
            
            