# april-5th

1. **Lowest Common Ancestor of a Binary Tree**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ### 递归的找,
        ### 这个函数本身的就和复杂,我们不需要helper
        ###　然后看了下返还的值是ｎｏｄｅ　

        if not root: # 还是先写终止
            return None
        if root == p or root ==q: ## 如果root 是我们的目标我们就返回该node
            return root
        left = self.lowestCommonAncestor(root.left,p,q) #　接着我们在左边也找
        right = self.lowestCommonAncestor(root.right,p,q) # 同上　 

        if left!=None and right!=None: #　如果左右有,返回改node 
            return root

        return left if left else right #　最低的意思，ｑ　ｐ不都在子树里面



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ### iterative 
        # DFS [1,2,3,q] [1,2,3,p] ,所以3 就是 lowest 
        # 返回的值是path 那就不是原本的function 可以做到了 


        if not root:
            return None
        ## 所以helper function 得到路线 
        def get_path(root,n):
            stack = []
            lastVisit = None
            while stack or root: 
                if root: # 一开始,一直将root and root.left
                    stack.append(root)
                    root = root.left
                else: # 这里就是没有left
                    node = stack[-1] # 这里并没有pop 出来 
                    if node.right and lastVisit != node.right:
                        root = node.right
                    else:
                        if node == n: # target
                            return stack
                        lastVisit = stack.pop()
                        root = None
            return stack

        pathP, pathQ = get_path(root, p), get_path(root, q)
        ans = None
        for x,y in zip(pathP,pathQ):
            if x == y:
                ans = x
            else:
                break
        return ans
```

