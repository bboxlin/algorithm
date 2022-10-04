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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null){
            return false;
        }
        int newsum = targetSum - root.val;
        if (root.left == null && root.right == null){
            return newsum == 0; 
        }
        boolean isLeftPathFound = hasPathSum(root.left, newsum);
        boolean isRightPathFound = hasPathSum(root.right, newsum);
        return isLeftPathFound || isRightPathFound;
    }
}