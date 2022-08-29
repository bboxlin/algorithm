class Solution {
    public String removeStars(String s) {
        StringBuilder ans = new StringBuilder();
        for (char c : s.toCharArray()){
            if (ans.length() > 0 && c == '*'){
                ans.setLength(ans.length() - 1);
            }else{
                ans.append(c);
            }
        }
        return ans.toString();
    }
}