class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # jstar代表模式串p中最后一次出现的星号的索引
        # istar代表s[:istar]这些字符全被jstar位置的这个星搞定了
        i, j = 0, 0
        iStar, jStar = -1, -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                iStar = i
                jStar = j
                j += 1
            elif iStar >= 0:
                iStar += 1
                i = iStar
                j = jStar + 1
            else:
                return False


        #字符串s已经被匹配完成，从此时开始j只能为*号才行
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
#大佬的python版本 这个题目的回溯就只有最外面一层(也可以说是最后一个*那一层)
#因为如果最后一个*无法解决的问题 前面的*更无法解决(贪心)
#我这里也给出了istar和jstar的意义