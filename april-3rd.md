# April 3rd

1. **Maximum Depth of Binary Tree**

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: # 终止
            return 0
        return max(self.maxDepth(root.right),self.maxDepth(root.left)) + 1 ## 返还和操作 + 1
```

1. **Construct Binary Tree from Inorder and Postorder Traversal**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        ## 首先这是有规律的 p 最后是root 
        ## 这里recursion传递的变量 本身的函数不够,其实是可以的,但是传递array 可能会超内存所以helper
        ## p 最后就是root, root 元素的左边就是left,右边就是right

        if not inorder or len(inorder)== 0 :
            return 

        def build(l, r):
            if l>r: # 终止条件
                return None
            v = postorder.pop() # 最后一位
            root = TreeNode(v)
            index = inorder.index(v) # 优化 空间换时间non-index

            root.right = build(index+1,r) # 用的是pop post 所以要right first
            root.left = build(l,index-1) # 前一个就是left
            return root

        return build(0,len(inorder)-1)
```

1. **Construct Binary Tree from Preorder and Inorder Traversal**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ###
        ## 和上题相比就是post 变成了pre
        ## 还是找规律
        ## pre 开头就是 root
        ## inorder 性质不变 

        if not preorder or len(inorder)==0:
            return 

        def build(l, r ):

            if l > r:
                return None # 照抄
            root = TreeNode(preorder.pop(0))
            index = inorder.index(root.val)
            root.left = build(l,index - 1) #　左边先
            root.right = build(index + 1,r)
            return root

        return build(0,len(inorder)-1)
```

1. **Validate Binary Search Tree**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ## 又是helper,因为原来的设定垃圾呀,只给传一个root
        ## helper ,目的是返还 boolean

        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True

            ## 另外这个判定只要有一个false 马上就不用再看了,所以找出所有False
            if node.val <= lower or node.val >= upper : ## 
                return False
            if not helper(node.right, node.val, upper):
                return False
            if not helper(node.left, lower, node.val):
                return False
            return True

        return helper(root)
```

