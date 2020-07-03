# 597 Subtree with Maximum Average

```text
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        ## 还是遍历.... 这个肯定选后序..
        
        
        self.ans_node = root
        self.avg = -float("inf")
        self.dfs(root)
        return self.ans_node
        
    def dfs(self,root):
        
        if not root:
            return (None, 0, 0)
        
        right_node,right_sum,right_count = self.dfs(root.right)
        left_node, left_sum ,left_count= self.dfs(root.left)
        ## 操作
        s = root.val + right_sum + left_sum
        c = 1 + left_count + right_count
        
        if s/c > self.avg:
            self.avg = s/c
            self.ans_node = root
        
        return root,s,c
```

