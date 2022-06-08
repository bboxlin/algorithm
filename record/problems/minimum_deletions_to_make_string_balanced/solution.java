class Solution {
    public int minimumDeletions(String s) {
        
        int n = s.length();

        int[] preB = new int[n];
        int[] backA = new int[n];

        for(int i = 1; i < n; i++){
            if(s.charAt(i - 1) == 'b'){
                preB[i] = preB[i - 1] + 1;
            }else{
                preB[i] = preB[i - 1];
            }
        }

        for(int i = n - 2; i >= 0; i--){
            if(s.charAt(i + 1) == 'a'){
                backA[i] = backA[i + 1] + 1;
            }else{
                backA[i] = backA[i + 1];
            }
        }
        // print(preB);
        // print(backA);
        int res = n;
        for(int i = 0; i < n; i++){
            res = Math.min(res, preB[i] + backA[i]);
        }

        return res;
    }
    
    public void print(int [] arr){
        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i]);
        }
        System.out.println();
    }
}

 