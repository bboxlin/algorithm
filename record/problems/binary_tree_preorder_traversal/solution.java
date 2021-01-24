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
    public List<Integer> preorderTraversal(TreeNode root) {
    //node left right
        // Stack <TreeNode> stack = new Stack();
        // List <Integer> list = new ArrayList();
        // while(!stack.empty() || root != null){
        //     while(root != null){ 
        //         //但凡有左,加入list
        //         list.add(root.val);
        //         stack.push(root);
        //         root = root.left;
        //     } 
        //     root = stack.pop(); //左为null，找前面的node
        //     root = root.right; //进入右边；
        // }
        // return list;
        
        // Stack <TreeNode> stack = new Stack<>();
        // List <Integer> list = new ArrayList<>();
        // if(root == null) return list;
        // stack.push(root);
        // while(!stack.empty()){ 
        //     root = stack.pop();//同步更改root;
        //     list.add(root.val);
        //     if(root.right != null) stack.push(root.right); //最早的right在最底下
        //     if(root.left != null) stack.push(root.left); /
        // }
        // return list;
        
        List<Integer> list = new ArrayList(); 
        return dfs(root, list);
    }
    public List<Integer> dfs (TreeNode root, List<Integer> list){
        if(root == null) return list;
        list.add(root.val);
        dfs(root.left, list);
        dfs(root.right, list);
        return list;
    }
}