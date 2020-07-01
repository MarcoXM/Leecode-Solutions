# june-5th

\103. Binary Tree Zigzag Level Order Traversal

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        ## 话说 最简单的层次遍历完... 
        ## 然后奇偶 翻转 
        ## 但是...这么做 肯定不是这题本意
        ans = []
        if not root: return ans
        q = collections.deque()
        q.append(root)
        depth = 0
        while q:
            ls = len(q)
            level = []
            depth += 1
            for _ in range(ls):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level:
                if depth & 1:
                    ans.append(level)
                else:
                    ans.append(level[::-1])
        return ans
```

\`[ Back](https://www.lintcode.com/ladder/1/)242. Convert Binary Tree to Linked Lists by Depth

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        ## 这不就是模板题...

        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            ls = len(q)
            dummy = ListNode(-1)
            head = dummy
            for _ in range(ls):
                node = q.popleft()
                if not node:
                    continue
                head.next = ListNode(node.val)
                head = head.next
                q.append(node.left)
                q.append(node.right)

            if dummy.next:
                ans.append(dummy.next)

        return ans
```

