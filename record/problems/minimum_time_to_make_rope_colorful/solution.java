class Solution {
    public int minCost(String colors, int[] neededTime) {
        int n = colors.length();
        int i = 0;
        int ans = 0;
        
        while (i < n){
            int j = i + 1;
            int curtotal = neededTime[i];
            int curmax = neededTime[i];
            while (j < n && colors.charAt(j) == colors.charAt(j-1)){
                curtotal += neededTime[j];
                curmax = Math.max(curmax, neededTime[j]);
                j += 1;
            }
            ans += curtotal - curmax; 
            i = j;
        }
        return ans;
    }
}