class Solution {
    
    public int[] twoSum(int[] nums, int target) {
    
        Map<Integer, Integer> myMap = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
             int value = target - nums[i];
            if(myMap.containsKey(value) && myMap.get(value) != i){
                //notice get (Object key) meaning to get the value in here is the index.
                return new int[] {i,myMap.get(value)};
            }
            myMap.put(nums[i],i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}