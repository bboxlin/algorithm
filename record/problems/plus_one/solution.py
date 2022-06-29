class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strint = ''.join([str(n) for n in digits])
        intnum = int(strint) + 1 
        return [int(n) for n in str(intnum)]
    
     # for i in range(len(digits)-1, -1, -1):
        #     digits[i] += 1
        #     if digits[i] < 10: return digits
        #     else: digits[i] %= 10
        # return [1] + digits
 

            