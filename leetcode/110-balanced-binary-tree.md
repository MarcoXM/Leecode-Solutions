# 110 Balanced Binary Tree

{% tabs %}
{% tab title="recursive" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(root):# helper 求高度
            if not root: #　终止
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        if abs(height(root.left) - height(root.right)) <= 1: # 左右子树都有,于是接着求
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
```
{% endtab %}
{% endtabs %}

