# 1800. Maximum Ascending Subarray Sum

```python
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                ans += nums[i]
            else:
                ans = nums[i]
                
            res = max(ans,res)
            
        return res
```

