# april-2nd

1. **Convert Sorted Array to Binary Search Tree**

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        ## 一个sub tree root.left, root, root.right 
        ## 永远选 seq 中间的num做root
        # BST 
        return self.helper(nums,0,len(nums)-1)

    def helper(self,nums,l,r):
        if l > r:
            return None

        mid = (l + r)//2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums,l,mid-1)
        root.right = self.helper(nums,mid+1,r)
        return root

        # O(N) recursive
```

1. **Surrounded Regions**

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 

        N,M = len(board),len(board[0])
        if N <=2 and M <= 2:
            return board

        from collections import deque
        q = deque() #这里也可以换成stack, stack或ｑ在这里真的就是个工具，容器
        for i in range(N):
            for j in range(M):
                if board[i][j] == "O" and i in [0,N-1] or j in [0,M-1]: # find the "O" near the boarder
                    q.append((i,j)) # 记录所有的location
        print(q)

        while q:
            x, y = q.popleft()
            if 0<=x<N and 0<=y<M and board[x][y] == "O" : # check it is "O" or not
                board[x][y] = "Other" # Temperally change O into Other
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:                
                    q.append((x+dx, y+dy)) # adding the near nodes 


        # And finally the "O" in the board are no relative in the board
        for i in range(N):
            for j in range(M):
                if board[i][j] =="O":
                    board[i][j] = "X"
                elif board[i][j] == "Other":
                    board[i][j] = "O"
```

1. **Path Sum**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 树要多想想递归
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        else:
            sum -= root.val # 现在的root 是存在的,做差
            if sum == 0 and not root.left and not root.right:
                return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
# O(N)

# DFS 复杂度是一样实际感觉比BFS快点    
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return []

        stack = []
        stack.append((root,sum))　#记录现在节点和target sum
        while stack:
            node, left_sum = stack.pop()
            if not node.left and not node.right and left_sum == node.val:
                return True
            if node.left:
                stack.append((node.left,left_sum - node.val))
            if node.right:
                stack.append((node.right,left_sum - node.val))
        return False
```

1. **Binary Tree Level Order Traversal**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        from collections import deque
        q = deque()
        q.append(root)
        level = 0
        while q:
            ans.append([])
            for i in range(len(q)):
                node = q.popleft() # 倒出里面的node
                ans[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return ans
    #O(N) 每一个都展开　


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        res = []
        return self.helper(root,0,[])

    def helper(self,root,level,res):

        if not root:
            return None
        # 添加　［］
        if len(res)<=level:
            res.append([]) ### 注意这里如果加多个[], 这个［］　就是为root的孩子准备的，当ｌｅｖｅｌ
        res[level].append(root.val)
        self.helper(root.left,level + 1,res)
        self.helper(root.right,level + 1,res)

        return res

    ## DFS 递归　依然是Ｏ(N)
```

1. **Delete Nodes And Return Forest**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:    
        ans = [] # 既然是返回一个list
        self.helper(root,True,to_delete,ans)
        return ans

    def helper(self,root,is_root,to_delete,ans):
        if not root:
            return None
        root_deleted = root.val in to_delete
        if is_root and not root_deleted: # 递归的参数在两个time_step
            ans.append(root) 

        root.left = self.helper(root.left,root_deleted,to_delete,ans)
        root.right = self.helper(root.right,root_deleted,to_delete,ans)

        return None if root_deleted else root
```

1. **Maximum Binary Tree**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        ## 这题目有毒
        ## 一开始就找最大,左边剩下的原array 元素构建左子树
        ## 右边剩下的原array 构建右子树 
        ## 重复 一直找剩下的 array里的最大的
        ## 递归传index not slice

        # 找max

        return self.helper(nums, 0, len(nums)) # 无需减1　遍历不会算－１

    def helper(self,nums,l,r):
        if l == r:
            return None

        max_index = self.get_max_index(nums, l, r)
        root = TreeNode(nums[max_index])
        root.left = self.helper(nums,l, max_index)
        root.right = self.helper(nums, max_index + 1, r)
        return root

    def get_max_index(self,nums,l,r):  # 这里的右边是不会取的index
        max_index = l
        for i in range(l,r):
            if nums[max_index] < nums[i]:
                max_index = i
        return max_index
```

