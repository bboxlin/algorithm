class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookup = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        patset = set()
        for word in words:
            pat = ""
            for c in word:
                idx = ord(c) - ord('a')
                pat += lookup[idx]
            patset.add(pat)
        return len(patset)