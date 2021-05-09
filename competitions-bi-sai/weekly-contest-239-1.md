# weekly-contest-239

前两题快，第三，四题想到







```python
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
## 先确定中点， 固定一个值，然后再优化另外一个值
        pre_sum = [0]
        nums = [0] + nums + [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
            
        
        left = [ i for i in range(len(nums))]
        right = [ i for i in range(len(nums))]
        
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
                
            stack.append(i)
          
        stack = []
        for i in range(len(nums) - 1, - 1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
                
            stack.append(i)
        # print(left, right )
        ans = 0
        for i in range(len(nums)):
            
            r = right[i] 
            if r != i:
                r -= 1
            
            l = left[i]
            if l!= i:
                l += 1
            ans = max(ans , nums[i] * (pre_sum[r + 1] - pre_sum[l]))
        return ans % 1000000007
```



 

