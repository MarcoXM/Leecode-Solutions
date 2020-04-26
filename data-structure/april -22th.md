## april-22th

\237. Delete Node in a Linked List

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
```



\56. Merge Intervals

```python
## 暴力, 处理边界
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals,key = lambda x:x[0])
        pre_l,pre_r = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if intervals[i][1] <= pre_r:
                continue
            elif intervals[i][0] <= pre_r:
                pre_r = intervals[i][1]
            elif intervals[i][0] > pre_r:
                ans.append([pre_l,pre_r])
                pre_l,pre_r = intervals[i]
            
        ans.append([pre_l,pre_r])
        return ans 
```

 Count Primes

```Python
class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [True] * n
        for i in range(2, n):
            j = 2
            while i * j < n:
                nums[i * j] = False
                j += 1
        res = 0
        for i in range(2, n):
            if nums[i]:
                res += 1
        return res ## 暴力写法居然过了
    
## 优化
class Solution:
    def countPrimes(self, n: int) -> int:
        nums = [True] * max(n, 2)
        nums[0], nums[1] = False, False
        x = 2
        while x * x < n:
            if nums[x]:
                p = x * x
                while p < n:
                    nums[p] = False
                    p += x
            x += 1
        return sum(nums) 
```



\2. Add Two Numbers

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(-1)
        flag = 0
        node = ans
        while l1 and l2:
            digit = (l1.val+l2.val + flag)
            if digit > 9:
                node.next = ListNode(digit%10)
                flag = 1
            else:
                node.next = ListNode(digit)
                flag = 0
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while l1 and not l2:
            digit = (l1.val+ flag)
            if digit > 9:
                node.next = ListNode(digit%10)
                flag = 1
            else:
                node.next = ListNode(digit)
                flag = 0
            node = node.next
            l1 = l1.next
        while l2 and not l1:
            digit = (l2.val + flag)
            if digit > 9:
                node.next = ListNode(digit%10)
                flag = 1
            else:
                node.next = ListNode(digit)
                flag = 0
            node = node.next
            l2 = l2.next
        if flag == 1:
            node.next = ListNode(flag)
        return ans.next
```



```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def helper(root):
            if not root:
                return 
            helper(root.left)
            ans.append(root.val)
            helper(root.right)
            
        ans = []
        helper(root)
        return ans 
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        ans = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            ans.append(node.val)
            root = node.right
        return ans
            
            
```

