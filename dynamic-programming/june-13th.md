## june-13th

\300. Longest Increasing Subsequence

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ## 输出长度 
        ## 定义子问题 长度为 N时,找出最长的子序列 
        ## dp[i] <- 从0 idx 开始 长度为i时最长的子序列长度
        
        ## 定义dp table 
        # dp = [] * len(nums) 
        ## 开始填表格
        ## 表格中任意cell 最小值为 1 
        dp = [1] * len(nums)
        ## 主循环肯定要有,不然怎么更新i
        for i in range(len(nums)):
            
            ## J 代表i 前面的数字,如果I 大于 J, 在table上更新结果
            ## 遍历i前面元素,不然怎么判定increasing
            
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
                    
                    
        return max(dp,default=0)
```

