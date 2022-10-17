class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        b = 0
        for ch in sentence:
            shift = ord(ch) - ord('a')
            b |= 1 << shift
        return b == (1 << 26) - 1 