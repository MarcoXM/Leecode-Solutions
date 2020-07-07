# 剑指 Offer 11. 旋转数组的最小数字

```python
class Solution:
    def minArray(self, nums: List[int]) -> int:
        ## 二分法
        ## nums[r] < nums[l]
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r ) //2
            if nums[r] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid + 1
            else:
                ## 不断往左边压缩边界，越不越界有外面的看着
                r -= 1
        return nums[l]

```

