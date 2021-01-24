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
    public List<Integer> inorderTraversal(TreeNode root) {
        //left node right
        // Stack <TreeNode> stack = new Stack<>();
        // List<Integer> list = new ArrayList<>();
        // while(!stack.empty() || root != null){
        //     while(root != null){
        //         stack.push(root);
        //         root = root.left;
        //     }//当最左边的child == null 退出
        //     root = stack.pop();  //root = 目前的node
        //     list.add(root.val);  //加入目前的node;
        //     root = root.right;   //root = 目前的右边child
        // }
        // return list;
      List<Integer> list = new ArrayList(); 
      return dfs(root, list);
    }
    public List<Integer> dfs (TreeNode root, List<Integer> list){
        if(root == null) return list;
        dfs(root.left, list);
        list.add(root.val);
        dfs(root.right, list);
        return list;
    }
}