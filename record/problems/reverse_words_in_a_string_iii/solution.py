class Solution:
    def reverseWords(self, s: str) -> str:
        def reversing(word):
            return "".join([word[i] for i in range(len(word)-1, -1, -1)])
            
        lst = s.split()
        for i, word in enumerate(lst):
            lst[i] = reversing(word)
        return " ".join(lst)