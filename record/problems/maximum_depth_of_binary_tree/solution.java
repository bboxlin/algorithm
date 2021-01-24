/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) { 
        
        
        // if(root == null) return 0;
        // Queue <TreeNode> q = new LinkedList();
        // int depth = 0;
        // q.add(root);
        // while(!q.isEmpty()){
        //     int size = q.size();
        //     for(int i = 0; i<size; i++){
        //         TreeNode cur = q.poll();
        //         if(cur.left != null) q.add(cur.left);
        //         if(cur.right != null) q.add(cur.right);
        //     }
        //     depth++;
        // }
        // return depth;
        return max(root,0);
         
    }
    public int max(TreeNode root, int sum){
        if(root == null) return sum;
        return Math.max(max(root.left,sum+1),max(root.right,sum+1));
    }
}