## april-16th

1383. **Maximum Performance of a Team**

```python
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ## 速度可以保持不变,但是效率是由团队中最小的人决定的.
        ## 一个环节效率底,后面进行不下去,
        es = sorted(zip(efficiency,speed))[::-1] # 按ｅ倒序,保证efficient 不断下降
        h = []
        ans = csum = 0
        for e,s in es: # 后面的人的ｅ　比较小
            heapq.heappush(h,s)
            csum += s
            if len(h) > k:
                csum -= heapq.heappop(h) # update current sum of the queue
            ans = max(ans,csum * e)
        return ans % (10**9 + 7)
    
    ## 典型的heap sort 套路,一开始sort复杂度NlogN,后面遍历NlogK ,N(logN + Log K)
```



1382.**Balance a Binary Search Tree**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []
        def getval(root):
            if not root: return 
            getval(root.left)
            values.append(root.val) #inorder 不用sort  
            getval(root.right)
        getval(root)
        
        def build(i, j):
            if i > j :
                return None
            mid = (i + j)//2
            root = TreeNode(values[mid])
            root.left = build(i,mid - 1)
            root.right = build(mid + 1,j)
            return root
        
        return build(0,len(values) - 1)
            
       # 复杂度 N,
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        roots = []
        def getval(root):
            if not root: return 
            getval(root.left)
            roots.append(root)
            getval(root.right)
        getval(root)
        
        def build(i, j):
            if i > j :
                return None
            mid = (i + j)//2
            root = roots[mid]
            root.left = build(i,mid - 1)
            root.right = build(mid + 1,j)
            return root
        
        return build(0,len(roots) - 1)
            
        ## 少了重建环节,速度更快
            
```

