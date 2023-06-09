class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        for ch in letters:
            if ch > target:
                res = ch
                break
                 
        return res
