class Solution {
    
    public int[] twoSum(int[] nums, int target) {
    
        Map<Integer, Integer> myMap = new HashMap<>();
        int [] ans = {-1, -1};
        for(int i = 0; i<nums.length; i++){
             int value = target - nums[i];
            if(myMap.containsKey(value)){
                ans[0] = i;
                ans[1] = myMap.get(value);
                return ans;
            }
            myMap.put(nums[i],i);
        }
        return ans;
    }
}