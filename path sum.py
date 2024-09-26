from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,newTargetSum):
            # Base case: if the tree is empty
            if not node:
                return False
            newTargetSum = newTargetSum + node.val 
            # If we reach a leaf node
            if not node.left and not node.right:
                return newTargetSum == targetSum
        
        # Recur for left and right subtrees with the updated targetSum
            
            return (self.dfs(node.left, newTargetSum) or
                self.dfs(node.right, newTargetSum))
        return dfs(root,0)
    
t=TreeNode()
s=Solution()
ans=s.hasPathSum([1,2,3], 5)
print(ans)
