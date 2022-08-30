class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx = 0
        pos = 0 
        while pos < len(number):
            if number[pos] == digit:
                idx = pos
                if pos + 1 < len(number) and number[pos+1] > digit:
                    break
            pos += 1
        return number[:idx] + number[idx+1:]
                