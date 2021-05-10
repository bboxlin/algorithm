class Solution {
    public String convert(String s, int numRows) {

        if(numRows <= 1 || numRows >= s.length()){
            return s;
        }
        
        int interval = 2*numRows - 2;
        String result = "";
        int n = 0;
        for(int row = 0; row < numRows; row++){
            for(int j = row; j<s.length(); j+=interval){
                result = result + s.charAt(j); 
                n++;
                int next = n*interval - row;
                if(row!=0 && row!=numRows-1 && next<s.length()){
                    result = result + s.charAt(next);
                }
            }
            n = 0;
        }
        return result;
    }
}