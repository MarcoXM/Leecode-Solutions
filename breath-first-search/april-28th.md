## april-28th

104. **Maximum Depth of Binary Tree**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))
    
   
```

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    if root == nil  {
        return 0
    }
    left := maxDepth(root.Left)
    right := maxDepth(root.Right)
    return 1 + max(left,right)

}   

func max(l, r int) int {
    if l >= r {
        return l
    } else {
        return r
    }
}
```







111. **Minimum Depth of Binary Tree**

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 1
        q = collections.deque()
        q.append(root)
        while q:
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                elif not node.left and not node.right :
                    return ans
                
            ans += 1
            
            
 class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        left = self.minDepth(root.left) 
        right = self.minDepth(root.right)
        if left == 0 or right == 0: # 并不是都没有儿子
            return left + right + 1
        return min(left, right) + 1
            
```



13. **Roman to Integer**

```python

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ans = 0
        if not s:
            return ans
        prev = 0
        ### 反向遍历
        for i in range(len(s)-1,-1,-1):
            if d[s[i]] < prev:
                ans -= d[s[i]]
            else:
                ans += d[s[i]]
                prev = d[s[i]]
            
        return ans 
```



```go

func romanToInt(s string) int {
    d := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
    var ans int
    var prev int
    if len(s) == 0 {
        return ans
    }
    for i:=len(s)-1; i>= 0 ; i-- {
        if d[s[i]] < prev{
            ans -= d[s[i]]
        } else {
            ans += d[s[i]]
            prev = d[s[i]]
        }
        
    }
    return ans
}   
```

