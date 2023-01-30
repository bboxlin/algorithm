class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(pstr):
            if int(pstr) == 0:
                return False 
            for i in range(len(pstr)):
                curnum = int(pstr[i])
                # try remove [1, curnum]
                for x in range(0, curnum):
                    newpstr = pstr[:i] + str(x) + pstr[i+1:]
                    # after I remove, newpstr == 0, I win
                    if dfs(newpstr) == False:
                        return True
            return False


        pstr = ''.join([str(num) for num in piles])
        return dfs(pstr)
        