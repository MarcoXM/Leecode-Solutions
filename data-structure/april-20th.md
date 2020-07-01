# april-20th

```python
# 1893. the Valid String
class Solution:
    """
    @param s: a String
    @return: if valid return "YES" else return "NO"
    """
    def isValid(self, s):
        # write your code here
        ## 统计结果一样,直接就是Yes,如果两个值大的值a>b a - 1 = b or b == 0 num of == 1 
        if not s:
            return "YES"

        dit = collections.defaultdict(int)
        dit2 = collections.defaultdict(list)
        for c in s:
            dit[c] += 1 

        for k,v in dit.items():
            dit2[v].append(k)
        if len(dit2) == 1:
            return "YES"
        elif len(dit2) > 2:
            return "NO"


        elif len(dit2) == 2:
            print(dit2)
            for k,v in dit2.items():
                if (dit2.get(k-1)!=None and len(dit2.get(k)) == 1) or (k == 1 and len(dit2.get(k)) == 1):
                    return "YES"
            return "NO"
```

1. **Symmetric Tree**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        ## 模板,终止,返回啥,操作啥
        if not root:
            return True
        return self.helper(root.left,root.right)

    def helper(self,l,r):
        if not l and not r:
            return True
        if l and r and (l.val == r.val):
            left = self.helper(l.left,r.right)
            right = self.helper(l.right,r.left)
            return left and right
        return False
```

