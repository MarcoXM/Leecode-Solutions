# April 4th

1. **Kth Largest Element in an Array**

```python
# 补
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## 首先要不quick sort 要不 merge 要不heapq

        p = random.choice(nums)
        nums1,nums2 = [],[]
        for i in range(len(nums)):
            if nums[i]<p:
                nums1.append(nums[i])

            elif nums[i]>p:
                nums2.append(nums[i]) # 根据p 来将 nums 分成两堆qs 是排了再分,dc是分了再排

        # len(nums1) + len(nums2) < len(nums)
        if k <= len(nums2): # 大的这堆里面的数字个数,比K多,那么我们的k就在里面
            return self.findKthLargest(nums2,k)

        if k > len(nums)-len(nums1): # 反之,K在小堆里面
            return self.findKthLargest(nums1,k -(len(nums)-len(nums1)))#更新K 值

        return p
```

1. **Balanced Binary Tree**

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

1. **Flatten Binary Tree to Linked List**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ### 统一node.right 就是 node.next
        ## 先用recursion 来做

        def t(root):
            if not root:
                return None
            vals.append(root)
            t(root.left)
            t(root.right)

        vals = []
        t(root) ## 这个我们就用递归把它们存下来了
        for i in range(len(vals) - 1):
            vals[i].left = None
            vals[i].right = vals[i+1]

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ### 统一node.right 就是 node.next
        ## 先用recursion 来做

        ## 先思考就是三个nodes 时的状态, 永远是root第一 left 次之,right last 
        # root.left.right = root.right
        # root.right = root.left

        ### 右 左 根  
        ### 右>左>根

        self.pre = None
        def t(root):
            if not root:
                return None 
            t(root.right) ## 会先执行一直往右
            t(root.left)
            root.left = None # 断开 
            #　print(self.pre)
            root.right = self.pre
            self.pre = root
        t(root)



class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ### 　   完全不递归 
        ### 那要用什么装root呢?
        stack = []
        stack.append(root)
        head = TreeNode(0)
        while stack:
            node = stack.pop()
            if not node:
                continue
            stack.append(node.right)
            stack.append(node.left) ## 后进先出
            head.right = node
            head.left = None
            head = node # 换下一个
```

1. **Kth Smallest Element in a BST**

```python
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        ### intuitive 就是inorder 的第K个

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]




class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        ### intuitive 就是preorder 的第K个

        stack = [root]

        while True:
            while root:
                stack.append(root)
                root = root.left ## 疯狂往左 
            root = stack.pop()
            k -= 1
            if not k:
                return root.val 
            root = root.left
            ## 更快的做法,不需要完整树
```

