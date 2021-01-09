# 228. Summary Ranges

```python
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ans = []
        if not nums: return ans 

        left = nums[0]
        right = nums[0]
        for i in range(1,len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                right = nums[i]

            else:
                ans.append(f"{left}->{right}" if left != right else str(left))
                left = nums[i]
                right = nums[i]
        ans.append(f"{left}->{right}" if left != right else str(left))
        return ans
        

```

