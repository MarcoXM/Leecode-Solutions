# june-2nd

\119. Pascals Triangle II

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ### 滚动数组

        if rowIndex == 0:
            return [1]
        ans = [1]
        for _ in range(rowIndex):
            ## 数组元素错位相减
            ans = [x + y for x,y in zip([0] + ans, ans + [0])]
        return ans
```

\459. Repeated Substring Pattern

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ## 第一想法count 找出pattern
        ## 然后发现... 很麻烦要分类讨论很多情况

        dp = [-1] * len(s) # 初始化必须-1, 因为 一旦j 是在首位不匹配,退无可退 
        ## 再者数组长度为什么是s,因为我们不知道patern 多长
        for i in range(1,len(s)):
            j = dp[i-1] # 读取

            ## 如果他不匹配,
            while j >= 0 and s[i] != s[j+1]:
                j = dp[j]  ## j 永远小于i, 为什么不是j+1,因为失败了

            if s[i] == s[j+1]: ##如果　str等于  patern(首字母)
                j += 1 ## patern 指针移位
                dp[i] = j
        ## 判断dp数组,前面-1的处,即为index,(如果后面没有-1出现)
        ## -1 part 数组长为s约数
        return dp[-1]>=0 and len(s)%(len(s) - (dp[-1] + 1))==0
```

