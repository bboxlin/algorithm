class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenS, lenP = len(s), len(p)
        output = []
        if lenS < lenP:
            return output 
        # s = "cbaebabacd", p = "abc"
        #       | |
        arr1, arr2 = [0]*26, [0]*26
        for i in range(lenP):
            idx1 = ord(p[i]) - ord('a')
            idx2 = ord(s[i]) - ord('a')
            arr1[idx1] += 1
            arr2[idx2] += 1
            
        if arr1 == arr2: 
            output.append(0)
        
        for rightPos in range(lenP, lenS):
            leftPos = rightPos - lenP 
            arr2[ord(s[leftPos]) - ord('a')] -= 1
            arr2[ord(s[rightPos]) - ord('a')] += 1
           
            if arr1 == arr2:
                output.append(leftPos + 1)
        
        return output
                