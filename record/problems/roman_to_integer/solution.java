class Solution {
    public int romanToInt(String s) {
        
        Map<Character, Integer> lookup = new HashMap<Character, Integer>();
        lookup.put('I', 1);
        lookup.put('V', 5);
        lookup.put('X', 10);
        lookup.put('L', 50);
        lookup.put('C', 100);
        lookup.put('D', 500);
        lookup.put('M', 1000);
        
        // I V
        //-1 +5
        int ans = 0;
        for (int i=0; i < s.length(); i++){
            
            if (i == s.length() - 1){
                ans += lookup.get(s.charAt(i));
            }else{
                int curVal = lookup.get(s.charAt(i));
                int nextVal = lookup.get(s.charAt(i+1));
                if (nextVal > curVal){
                    ans -= curVal;
                }else{
                    ans += curVal;
                }   
            }
        }
        return ans;
    }
}