class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnter = defaultdict(int)
        for domain in cpdomains:
            cnt, curdomain = domain.split()
            cnt = int(cnt)
            cnter[curdomain] += cnt
            for i in range( len(curdomain) ):
                if curdomain[i] == '.':
                    subdomain = curdomain[i+1:]
                    cnter[subdomain] += cnt 
        
        ans = []
        for domain, cnt in cnter.items():
            ans.append( str(cnt) + " " + domain )
        return ans