class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        # key = 已经创建过的文件夹名
        # val = k ：同名的文件数量
        
        # (k) , k增长的
        ans = []
        hashmap = {}
        for name in names:            
            if name not in hashmap.keys():
                ans.append(name)
                hashmap[name] = 0
            else:
                k = hashmap[name]
                modifiedName = name
                while modifiedName in hashmap.keys():
                    k += 1
                    modifiedName = name + '(' + str(k) + ')'
                ans.append(modifiedName)
                hashmap[name] = k
                hashmap[modifiedName] = 0
        return ans
                
                
                    
                