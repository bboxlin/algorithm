class Solution:
    def subarraysWithKDistinct(self, arr: List[int], k: int) -> int:
        def atMostk(arr, k):
            n = len(arr)
            freq = [0]*(n+1)
            left, right,count, res = 0,0,0,0
            while(right < n):
                if freq[arr[right]] == 0: count += 1
                freq[arr[right]] += 1
                right += 1

                while count > k:
                    freq[arr[left]] -= 1
                    if freq[arr[left]] == 0: count-=1
                    left += 1
                res += right - left;
            return res
        
        return atMostk(arr,k) - atMostk(arr,k-1)
 