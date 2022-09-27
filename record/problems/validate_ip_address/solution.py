class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkIpv4(lst):
            if len(lst) != 4: return "Neither"
            for strnum in lst:
                try:
                    intnum = int(strnum)
                    if intnum < 0 or intnum > 255 or str(intnum) != strnum:
                        return 'Neither'
                except:
                    return 'Neither'
            return 'IPv4'
        def checkIpv6(lst):
            if len(lst) != 8: return "Neither"
            content = '0123456789abcdefABCDEF'
            for stritem in lst:
                if len(stritem) < 1 or len(stritem) > 4:
                    return 'Neither'
                for c in stritem:
                    if c not in content:
                        return 'Neither'
            return 'IPv6'
        if queryIP.count('.') == 3:
            lst = queryIP.split('.')
            return checkIpv4(lst)
        elif queryIP.count(':') == 7:
            lst = queryIP.split(':')
            return checkIpv6(lst)
        else:
            return "Neither"