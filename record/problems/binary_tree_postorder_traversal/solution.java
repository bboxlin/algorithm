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
    public List<Integer> postorderTraversal(TreeNode root) {
        // //left right node  最后一个是root;
        // Stack <TreeNode> stack1 = new Stack();
        // Stack <TreeNode> stack2 = new Stack();
        // List <Integer> list = new ArrayList();
        // if(root == null) return list;
        // stack1.push(root); 
        // while(!stack1.empty()){
        //     TreeNode cur = stack1.pop();
        //     stack2.push(cur);
        //     if(cur.left != null) stack1.push(cur.left);
        //     if(cur.right != null) stack1.push(cur.right);
        // }
        // while(!stack2.empty()){
        //     TreeNode data = stack2.pop();
        //     list.add(data.val);
        // }
        // return list;
      List<Integer> list = new ArrayList(); 
      return dfs(root, list);
    }
    public List<Integer> dfs (TreeNode root, List<Integer> list){
        if(root == null) return list;
        dfs(root.left, list); 
        dfs(root.right, list);
        list.add(root.val);
        return list;
    }
}