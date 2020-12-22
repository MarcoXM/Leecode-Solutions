# 110 Balanced Binary Tree

{% tabs %}
{% tab title="O\(N\)" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if self.checkDepth(root) == -1: return False
        
        return True
        
        
    
    def checkDepth(self, root):
        if not root : return 0
        left = self.checkDepth(root.left)
        if left == -1:return -1
        right = self.checkDepth(root.right)
        if right == -1 :return -1
        if abs(left - right) > 1:return -1
        else:
            return max(left, right) + 1
        
        
        
        
    
        
```
{% endtab %}

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
     ight(root.left), height(root.right)) + 1

        if not root:
            return True
        if abs(height(root.left) - height(root.right)) <= 1: # 左右子树都有,于是接着求
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

        
```
{% endtab %}
{% endtabs %}

