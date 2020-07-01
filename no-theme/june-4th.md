# june-4th

\662. Maximum Width of Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ## 题目都说了 full binary tree
        ## 那就bfs 

        q = collections.deque()
        q.append((root,0))
        ans = 0
        while q:
            ls = len(q)
            level = []
            for _ in range(ls):
                node, posistion = q.popleft()
                level.append(posistion)
                if node.left:
                    q.append((node.left,posistion*2))
                if node.right:
                    q.append((node.right,posistion*2 + 1))
            ans = max(ans,level[-1] - level[0] + 1)

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
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        if not root: ## 因为我node 也做了self,以后还是要避免
            return 
        self.s = -float("inf")
        self.ans_nodes = root
        self.dfs(root)
        return self.ans_node


    def dfs(self, root):

        if not root:
            return 0, None

        right_s, right_node = self.dfs(root.right)
        left_s, left_node = self.dfs(root.left)

        s = root.val + right_s + left_s

        if s > self.s:
            self.s = s
            self.ans_node = root

        return s, root
```

