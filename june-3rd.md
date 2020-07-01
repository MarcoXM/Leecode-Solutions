# june-3rd

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def convertBST(self, root: TreeNode) -> TreeNode:

        ## 读题,
        ## return Root
        ## 想想什么遍历
        ## 这是平衡二叉树 
        ## 右 root 左

        if not root:
            return

        self.convertBST(root.right)
        original = root.val
        root.val += self.res
        self.res += original
        self.convertBST(root.left)

        return root

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def convertBST(self, root: TreeNode) -> TreeNode:

        ## 读题,
        ## return Root
        ## 想想什么遍历
        ## 这是平衡二叉树 
        ## 右 root 左
        ## 既然知道遍历的方式,迭代答案就呼之欲出
        ans = root
        s = 0
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.right
            root = stack.pop()
            s += root.val
            root.val = s
            root = root.left

        return ans
```

```python
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

