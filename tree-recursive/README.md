# Tree-recursive

1. **找整个递归的终止条件：递归应该在什么时候结束？**
2. **找返回值：应该给上一级什么返回值？**
3. **本级递归应该做什么：在这一级递归中，应该完成什么任务？**

## 树的基本特征

1. 为什么要有树:
   1. 树的查找是log\(N\)
2. 对与树这个数据结构的操作只有:
   1. 看值,
   2. 看左子树
   3. 看右子树

## 通用模板

```python
def traverse(root):
    ## 对root 的操作,你可以提取值,判定,返还root
    ## 对root 的子代的操作
    traverse(root.left)  ### 这里可以 类比二分的 low 和 high 
    traverse(root.right)



def addOne(root):
    if not root:
        return 
    root.val += 1 ## 改这里 
    addOne(root.left)
    addOne(root.right)

    ## 以上将所有的 树里面的值加上了1
```

### 来个例子

[Leetcode Same Tree](https://leetcode.com/problems/same-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        ## 返回 boolean值
```

[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None #　找终止条件

        # 本级递归应该做什么
        root.left , root.right = root.right, root.left # 操作就是交换位置 
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root　# 找返回值
```

[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root: # 终止 
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # 返回和操作
```

## 为什么需要helper function

* 因为操作过于复杂
* 还有要返回的参数过多

[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        if not root:
            return True
        if abs(height(root.left) - height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

        ## Helper function 换回的是root  的高度
        return self.isBalanced(root.left) and self.isBalanced(root.right)
```

[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.helper(root,-2**32,2**32)

    def helper(self,root,min,max):
        if not root:
            return True
        if root.val >= max or root.val<=min:
            return False

        return self.helper(root.right,root.val,max) and self.helper(root.left,min,root.val)
```



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        else:
            if sum == root.val and not root.left and not root.right:
                return True
                
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
            ## 明白一个函数的作用并相信它能完成这个任务，千万不要试图跳进细节
        ## 这个函数在root 上可以完成的事情,在root.left 或者说在rootright也能完成. 要对孩子有自信!
```





1. 二叉树算法的原则，把当前节点要做的事做好，其他交给递归框架，不用当前节点操心
2. 如果当前节点会对下面的子节点有整体影响，可以通过helpFunction辅助函数设计返回值接口，携带更多的参数传递信息。
3. BST和AVL树的验证方法

## 回溯

```python
result = []
function backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 of 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```

* 如果具体问解的个数，问最优、最先、最短，一般来讲用dp来做，问所有的解的集合 就用DFS

## DFS

```python
result： 所有结果集
list： 当前的单个解    （result和list会在DFS的过程中不断更新）
pos：记录当前处理的位置
visited：结点有无访问状态（求最优路径）
if(condition) 退出条件
```

[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right: # 剩下的)多于(
            self.dfs(res, left, right - 1, path + ')')
```

[994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer
```

