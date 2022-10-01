class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int [] dp = new int[n+1];
        dp[0] = 1;
        for (int i = 1; i<=n; i++){
            if (i == 1){
                dp[i] = s.charAt(i-1) != '0' ? 1 : 0;
            }else{
                int prevOne = Integer.valueOf(s.substring(i-1, i));
                int prevTwo = Integer.valueOf(s.substring(i-2,i));
                if (prevOne >= 1 && prevOne <= 9){
                    dp[i] += dp[i-1];
                }
                if (prevTwo >= 10 && prevTwo <= 26){
                    dp[i] += dp[i-2];
                }
            }
        }
        return dp[n];

    }
}