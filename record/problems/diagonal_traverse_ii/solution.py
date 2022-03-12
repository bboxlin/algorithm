class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        data = collections.defaultdict(list)
        R = len(nums)
        for i in range(R):
            C = len(nums[i])
            for c in range(C):
                key = i + c 
                data[key].append(nums[i][c])
        res = []
        for k, lst in data.items():
            diag_lst = reversed(lst)
            res += diag_lst
        return res
            
                
                
            