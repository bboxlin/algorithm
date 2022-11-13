class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        # lcm(a, b) = a * b / gcd(a, b). 
        def lcm(a,b):
            def gcb(a,b):
                if b == 0:
                    return a
                return gcd(b, a % b);
            return a*b // gcd(a,b)
        
        
        cnt = 0
        n = len(nums)
        for i in range(n):
            curlcm = 1
            for j in range(i, n):
                curlcm = lcm(curlcm, nums[j])
                if curlcm == k:
                    cnt += 1
                if curlcm > k:
                    break
        return cnt
                