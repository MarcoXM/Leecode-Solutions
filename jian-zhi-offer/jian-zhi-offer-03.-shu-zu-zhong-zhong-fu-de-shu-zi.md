# 剑指 Offer 03. 数组中重复的数字

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        ## 先问面试官要时间/空间需求！！！
        ## 只是时间优先就用字典，
        ## 还有空间要求，就用指针+原地排序数组，
        ## 如果面试官要求空间O(1)并且不能修改原数组，还得写成二分法！！！
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
        ## 这个最优解法，改变了input
```

