# Question: Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        def dfs(root, low, high):
            if root == None:
                return 
            if low <= root.val <= high:
                ans[0] += root.val
                dfs(root.left, low, high)
                dfs(root.right, low, high)
            
            elif root.val > high:
                dfs(root.left, low, high)
            elif root.val < low:
                dfs(root.right, low, high)
           
        
        ans = [0]
        dfs(root, low, high)
        return ans[0]
