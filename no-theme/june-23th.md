## june-23th

\238. Product of Array Except Self

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        ans = [1]
        ## 数组操作, 前缀积
        for i in range(len(nums) - 1):
            ans.append(product * nums[i])
            product = ans[-1]
        ## get the left product
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * product
            product = nums[i] * product
            
        return ans
```

\31. Next Permutation

```python

class Solution:
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## 这其实就是做加法..
        ## 观察... 相邻升序交换位置
        to_end = False
        ## 找到要换的small number
        i = len(nums) - 2
        while i > -1:
            if nums[i] <  nums[i+1]:
                to_end = True
                break
            i -= 1
        if not to_end:
            nums.sort()
        ## 找到要换big number
        for j in range(len(nums) - 1,i,-1):
            if nums[j] > nums[i]:
                break
        
        nums[i],nums[j] = nums[j],nums[i]
        ## 排序.. 写个快排呗, 其实直接换就好了,不用qsort 更快
        self.qsort(i+1,len(nums)-1,nums)
        
                
    def qsort(self,i, j, nums):
        l, r = i, j
        p = (l + r)//2
        m = nums[p]
        while l <= r:
            while l <= r and nums[l] < m:
                l += 1
            while r <=r and nums[r] > m:
                r -= 1
            if l <= r:
                nums[l],nums[r] = nums[r],nums[l]
                r -= 1
                l += 1
            self.qsort(i,r,nums)
            self.qsort(l,j,nums)
            
```



