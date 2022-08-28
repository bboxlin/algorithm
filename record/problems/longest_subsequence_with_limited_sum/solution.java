class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        int [] ans = new int [queries.length];
        int [] presum = new int [nums.length];
        Arrays.sort(nums); 
        int psum = 0;
        int idx = 0;
        for (int num: nums){
            psum += num;
            presum[idx++] = psum;
        }
        
        for (int k = 0; k < ans.length; k++){
            int l = 0;
            int r = presum.length - 1;
            while (l <= r){
                int mid = (l + r) / 2;
                if (presum[mid] <= queries[k]){
                    ans[k] = Math.max(ans[k], mid+1);                    
                    l = mid + 1;
                }else{
                    r = mid - 1;
                }
            }
        }
        
        return ans;
        
        
    }
}