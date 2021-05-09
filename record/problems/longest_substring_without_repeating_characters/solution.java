class Solution {
    
    public int lengthOfLongestSubstring(String s) {  

        HashMap <Character, Integer> map = new HashMap<>();
        
        int l = 0;
        int max = 0;      
        
        for(int r = 0; r<s.length(); r++){
            char cur = s.charAt(r);
            if(map.containsKey(cur) && map.get(cur)>=l){
                l = map.get(cur) + 1;
            }
            map.put(cur,r);
            max = Math.max(max, r-l+1);
        }
        return max;
    }
}
    
    
  
    
    
    