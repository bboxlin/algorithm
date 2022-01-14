class Solution:
    def isHappy(self, n: int) -> bool:
        
        '''
        Gets the next value
        '''
        def get_value(x):
            ans = 0
            while x:
                rem = x % 10
                x = x // 10
                ans += rem**2
            return ans
        
        '''
        Check if n == 1
        '''
        exist = set()        
        while n != 1:
            if n in exist:
                return False
            exist.add(n)
            n = get_value(n)
        return True
        
        
        