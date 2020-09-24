# Untitled

{% tabs %}
{% tab title="中序优化" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        pre = None
        maxCount = 0
        count = 0
        
        def update(val):
            nonlocal pre,maxCount,count,ans
            if val != pre:
                count = 1
                pre = val
                
            else:
                count += 1
                if count > maxCount:
                    ans = [val]
                    maxCount = count

                elif count == maxCount:
                    ans.append(val)
                pre = val
            # print(ans)

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            update(root.val)
            dfs(root.right)
        
        dfs(root)
        return ans
```
{% endtab %}

{% tab title="暴力" %}
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        path = []
        def dfs(root):
            if not root:
                return
            path.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        max_ = 0
        dit = {}
        for r in path:
            dit[r] = dit.get(r,0) + 1
            max_ = max(max_,dit[r])

        return [k for k in dit.keys() if dit[k] == max_]
```
{% endtab %}
{% endtabs %}

