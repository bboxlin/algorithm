class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        cha_list = list(palindrome)
        for i in range(len(cha_list)//2):
            if cha_list[i] != 'a':
                cha_list[i] = 'a'
                return "".join(cha_list)
        cha_list[-1] = 'b'
        return "".join(cha_list)
 
        