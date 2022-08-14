class Solution:
    def sortArray(self, N: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            leftarr = mergeSort(arr[:len(arr)//2])
            rightarr = mergeSort(arr[len(arr)//2:])
            
            i, j, k = 0, 0, 0
            while i < len(leftarr) and j < len(rightarr):
                if leftarr[i] < rightarr[j]: 
                    arr[k] = leftarr[i]
                    i += 1
                else: 
                    arr[k] = rightarr[j]
                    j += 1
                k += 1

            while i < len(leftarr):
                arr[k] = leftarr[i]
                i += 1
                k += 1

            while j < len(rightarr):
                arr[k] = rightarr[j]
                j += 1
                k += 1
            
            return arr
                    
        return mergeSort(N)
    
 
   