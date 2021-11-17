class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def divide_conquer(arr):
            if len(arr) > 1:
                mid = len(arr) >> 1
                l = divide_conquer(arr[:mid])
                r = divide_conquer(arr[mid:])
                combine(arr, l, r)
            return arr
        
        def combine(arr, left, right):
            i = 0 
            while left and right:
                if left[0] > right[0]:
                    arr[i] = left.pop(0)
                else:
                    arr[i] = right.pop(0)
                i += 1
            while right:
                arr[i] =right.pop(0)
                i+=1
            while left:
                arr[i] = left.pop(0)
                i+=1          
        return divide_conquer(nums)[k-1]
        
            
        