class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort() 
        psum = 0
        psum_lst = [] 
        for n in nums:
            psum += n
            psum_lst.append(psum)
         
        n = len(nums)
        m = len(queries)
        ans = [0]*m 
 
        for k in range(m):
            l, r = 0, n-1
            while l <= r:
                mid = (l + r) // 2
                if psum_lst[mid] <= queries[k]:
                    ans[k] = max(ans[k], mid+1)
                    l = mid + 1
                else:
                    r = mid - 1
        return ans
                
                    