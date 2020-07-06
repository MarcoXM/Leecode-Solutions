# 剑指 Offer 07. 重建二叉树

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 :
            return
        idx = inorder.index(preorder[0])
        
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:idx + 1],inorder[0:idx])
        root.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return root



    def build(self, left,right, preorder, inorder):
        if left == right:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.build( left,idx-1, preorder, inorder)
        root.right = self.build(idx + 1,right, preorder, inorder)

        return root
```

