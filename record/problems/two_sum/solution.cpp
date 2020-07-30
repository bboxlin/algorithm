class Solution {
    
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result (2);
        for(int i = 0; i<nums.size();i++){
            for(int j = i+1; j<nums.size();j++){
                if(nums[i] + nums[j] == target){
                    result[0] = i;
                    result[1] = j;
                    //we are returning the index that add up equals to the target for nums                       vector by using vector result to represents; 
                }
            }     
        }
        return result;
    }
};