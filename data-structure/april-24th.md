## april-24th

Reverse Words in a String II

```python

class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        w_list = str.split()
        
        
        l,r = 0,len(w_list)-1
        while l<r:
            w_list[l],w_list[r] = w_list[r],w_list[l]
            l += 1 
            r -= 1
        return " ".join(w_list)

```

```python

class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        w_list = str.split()
        
        new = []
        def helper(idx):
            if idx < 0:
                return
            new.append(w_list[idx])
            helper(idx-1)
            
            
        helper(len(w_list)-1)
        return " ".join(new)

```



```go

func reverseWords(str string) string {
    w_list := strings.SplitAfter(str, " ")
    j := len(w_list) - 1
    for i < j{
        w_list[i],w_list[j] = w_list[j], w_list[i]
        i++
        j--
    }
    result := strings.Join(w_list," ")
    return result
}	
```





654. Maximum Binary Tree

```python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        ## 每次用左右sub array max value 建树
        ## 这题不是做过了嘛
        return self.helper(nums, 0, len(nums)) 
        
    def helper(self,nums,l,r):
        if l == r:
            return None
        
        max_index = self.get_max_index(nums, l, r) # helper 获得max_index
        root = TreeNode(nums[max_index])
        root.left = self.helper(nums,l, max_index)
        root.right = self.helper(nums, max_index + 1, r)
        return root
        
    def get_max_index(self,nums,l,r): 
        max_index = l
        for i in range(l,r):
            if nums[max_index] < nums[i]:
                max_index = i
        return max_index
        
```

