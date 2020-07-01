# may-16th

\513. Find Bottom Left Tree Value

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ## 迭代层次遍历
        ## 不需要判断那个node 是不是左子树,B tree优先满足左边
        q = deque()
        q.append(root)
        res = []
        while q :
            l = len(q)
            level = []
            for _ in range(l):
                node = q.popleft()
                if not node:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if len(level) > 0:
                res[:] = level # 优化
        return res[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ## 迭代层次遍历
        ## 不需要判断那个node 是不是左子树,B tree优先满足左边
        ## DFS 
        def dfs(root,level):
            if not root:
                return

            if level == len(res):
                res.append([])   
            res[level].append(root.val)
            dfs(root.left,level + 1)
            dfs(root.right,level + 1)
        res = []
        dfs(root,0)
        return res[-1][0]



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ## 迭代层次遍历
        ## 不需要判断那个node 是不是左子树,B tree优先满足左边
        ## DFS 
        ## 迭代 DFS 感觉还能优化....
        stack = [(root,0)]
        res = [-1,None] #　原本想map(int:list)记录，优化
        while stack:
            node,level = stack.pop()
            if not node:
                continue
            if level > res[0]:
                res[1] = node.val
                res[0] = level
            stack.append((node.right,level + 1)) # 先进后出
            stack.append((node.left,level+1))

        return res[1]
```

\333. Largest BST Subtree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        ### 不符合复杂度，符合软件工程模块化．．．
        if not root:
            return 0

        if self.isValidBST(root):
            return self.count(root)
        return max(self.largestBSTSubtree(root.left),self.largestBSTSubtree(root.right))

    ## 数数　
    def count(self,root):
        if not root:
            return 0
        return self.count(root.left) + self.count(root.right) + 1

    ##　判定
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        pre = None  
        while root or stack != []:
            while root:
                stack.append(root)
                root = root.left # 左儿子,一直狂塞，到最左边
                # print(stack)
            root = stack.pop()
            if pre!= None and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True
    ## 复杂度 0(N^2)
```

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        ans = self.dfs(root,-float('inf'),float('inf'))
        return ans[0]

    def dfs(self, root, MIN, MAX):
        if not root:
            return (0,MIN,MAX)
        ## 先操作 儿子, 然后再到爸爸, 就是后序遍历 
        left = self.dfs(root.left, MIN, MAX)
        right = self.dfs(root.rght, MIN, MAX)

        if root.val > left[2] and root.val < right[1]:
            return (left[0] + right[0] + 1, min(root.val,left[1]), max(root.val,right[2]))
        else:
            return max(left[0],right[0]),MIN,MAX
```

