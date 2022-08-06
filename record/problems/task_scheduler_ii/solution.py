class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # tasks = [1,2,1,2,3,1], space = 3

                
        # dic = {}
        # day = 0 
        # for t in tasks:
        #     if t in dic.keys():
        #         day = max(day+1, dic[t] + space + 1)
        #     else:
        #         day += 1
        #     dic[t] = day
        # return day
        
        dic = {}
        day = 0 
        for t in tasks:
            if t in dic.keys() and day - dic[t] < space:
                day = dic[t] + space + 1
            else:
                day += 1
            dic[t] = day
        return day
            
        
       
            