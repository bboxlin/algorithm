class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def dfs(i, acc):
            if i == len(digits):
                res.append(acc)
                return 
            d = digits[i]
            for cha in graph[d]:
                dfs(i+1, acc+cha)
            


        if not digits:
            return []
        graph = {'2':'abc',
                 '3':'def',
                 '4':'ghi',
                 '5':'jkl',
                 '6':'mno',
                 '7':'pqrs',
                 '8':'tuv',
                 '9':'wxyz'}
        res = []
        dfs(0, "")
        return res