class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        
        stack = stack[:len(stack) - k] # if k > 0, then this removes the right end numbers
        str_res = "".join(stack) # to int and back to str, to clear the leading 0
        return str(int(str_res)) if str_res else "0"
            