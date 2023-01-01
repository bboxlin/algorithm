class Solution:
    def confusingNumber(self, n: int) -> bool:
        res = ""
        sn = str(n)
        for i in range( len(sn)-1, -1, -1 ):
            if sn[i] in "23457":
                return False 
            if sn[i] == "6":
                res += "9"
            elif sn[i] == "9":
                res += "6"
            else:
                res += sn[i]
        return res != sn 
