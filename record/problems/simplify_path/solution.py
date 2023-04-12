class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for item in path.split('/'):
            print(item)
            if item == '..':
                if res: res.pop()
            elif item == '.' or not item:
                continue
            else:
                res.append(item)
        return "/" + "/".join(res)