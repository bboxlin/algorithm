class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_lst= list(str(num))
        # to store 0-9 as key and corresponding index
      
        memo = {}    
        for idx, number in enumerate(num_lst):
            memo[number] = idx

        for i in range(len(num_lst)):
            cur_int = int(num_lst[i])
         
            for j in range(9, cur_int, -1):
                j_str = str(j)
 
                # if such number exist in memo, and its index is greater than i, we swap
                if j_str in memo and memo[j_str] > i:
                    num_lst[i], num_lst[memo[j_str]] = num_lst[memo[j_str]], num_lst[i]
                    return int("".join(num_lst))
        return num
            
            
        