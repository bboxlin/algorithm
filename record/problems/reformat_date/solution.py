class Solution:
    def reformatDate(self, date: str) -> str:
        monthDic = {"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', "May":'05', "Jun":'06', "Jul":'07', "Aug":'08', "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        dataList = date.split()
        ans = []
        for i in range(len(dataList)-1, -1, -1):
            
            # year
            if i == 2:
                curyear = dataList[i]
                ans.append(curyear)
            # month
            elif i == 1:
                curmonth = dataList[i]
                digitMonth = monthDic[curmonth]
                ans.append(digitMonth)
            # day
            else:
                curday = dataList[i]
                curday = curday[:-2]
                if len(curday) == 1:
                    curday = '0' + curday
                ans.append(curday)
        return "-".join(ans)
        