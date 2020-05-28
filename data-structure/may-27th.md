## may-27th

\155. Min Stack

```python

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            min_ = self.stack[-1][1]
            if x < min_:
                self.stack.append((x,x))
            else:
                self.stack.append((x,min_))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```



\199. Binary Tree Right Side View

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ## 用bfs 直接就可以做
        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            ls = len(q)
            level = []
            for _ in range(ls):
                node = q.popleft()
                if not node:
                    continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                ans.append(level)
                
        return list(map(lambda x : x[-1],ans))
```

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ## 递归做法不太会,iter dfs 比较好(ˇˍˇ) 想～
        ##
        stack = [(root,0)]
        ans = collections.defaultdict(int)
        while stack:
            node, level = stack.pop()
            if not node:
                continue
            if level not in ans:
                ans[level] = node.val
            if node.left:
                stack.append((node.left,level + 1))
                
            if node.right:
                stack.append((node.right,level+1))
            
        return ans.values()
```

