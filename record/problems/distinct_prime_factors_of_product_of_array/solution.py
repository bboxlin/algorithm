class Solution:
    """
    The Fundamental Theorem of Arithmetic states that 
    every natural number greater than 1 can be written as a product of prime numbers
    """

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def isPrime(number):
            if number == 2:
                return True 
            for num in range(2, number//2+1):
                if number % num == 0:
                    return False 
            return True 

        primes = []
        for val in range(2, 1000):
            if isPrime(val):
                primes.append(val)

        ans = set()
        for num in nums:
            for prime in primes:
                if num % prime == 0:
                    ans.add(prime)  
            
        
 
        return len(ans)

