class Solution:
    def entityParser(self, text: str) -> str:
        dic = {
            "&quot;":"\"",
            "&apos;":"\'",
            "&amp;":"&",
            "&gt;":">",
            "&lt;":"<",
            "&frasl;":"/"
        }
        ans = ""
        n = len(text)
        l = 0
        while l < n:
            # forward scanning
            if text[l] == "&":
                temp = text[l]
                r = l + 1
                while r < n and text[r] != ";" and text[r] != "&":
                    temp += text[r]
                    r += 1
                # find ;
                if r < n and text[r] == ";":
                    temp += text[r]
                    if temp in dic:
                        ans += dic[temp]
                    else:
                        ans += temp
                    l = r + 1
                # not find ;
                else:
                    ans += temp
                    l = r
            # just scanning
            else:
                ans += text[l]
                l += 1
        return ans