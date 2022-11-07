class Solution:
    def maximum69Number (self, num: int) -> int:
        
        goodnum = ""
        once = True
        for n in str(num):
            if n == '6' and once :
                goodnum += '9'
                once = False
            else:
                goodnum += n
        return int(goodnum)
                