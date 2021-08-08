from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        lst = SortedList()
        res = []
        
        for n in nums[::-1]:
            #search n's left in lst
            ans = SortedList.bisect_left(lst,n)
            res.append(ans)
            lst.add(n)
            
        return reversed(res)