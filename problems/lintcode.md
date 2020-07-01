# Lintcode

```text
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
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        ## 还是遍历.... 这个肯定选后序..
        
        
        self.ans_node = root
        self.avg = -float("inf")
        self.dfs(root)
        return self.ans_node
        
    def dfs(self,root):
        
        if not root:
            return (None, 0, 0)
        
        right_node,right_sum,right_count = self.dfs(root.right)
        left_node, left_sum ,left_count= self.dfs(root.left)
        ## 操作
        s = root.val + right_sum + left_sum
        c = 1 + left_count + right_count
        
        if s/c > self.avg:
            self.avg = s/c
            self.ans_node = root
        
        return root,s,c
```

```text
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

```text

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        
        ### 这题很迷...
        ### 没有空间,时间限制,不就是easy难度了 
        
        nums.sort()
        print(nums)
        l,r = 0,len(nums)-1
        ans = 0
        while l < r:
            while l > 0 and nums[l-1] == nums[l]:
                l += 1
            while r < len(nums)-1 and nums[r+1] == nums[r]:
                r -= 1
            
            ## 测试例子确实很棒
            if l < r and nums[l] + nums[r] == target:
                print(l,r)
                ans += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
                
        return ans
```

