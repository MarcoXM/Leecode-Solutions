## june-12th

\1736. Throw garbage

```python
class Solution:
    """
    @param BagList: the weight of all garbage bags.
    @return: an integer represent the minimum number of times.
    """
    def Count_ThrowTimes(self, BagList):
        #
        BagList.sort()
        ans = 0
        j = 0
        i = len(BagList) - 1
        while j <= i :
            if BagList[j]+ BagList[i] <= 3:
                ans += 1 
                i -= 1
                j += 1 
            elif BagList[j]+ BagList[i] > 3:
                ans += 1
                i-=1
        
        return ans 
        
```

\902. Numbers At Most N Given Digit Set

```python

class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        ### 
        ### 至顶而下的写法
        s = str(N)
        len_N = len(s)
        len_D = len(D)
        ans = 0
        
        ## 退一位所有可能
        for i in range(1,len_N):
            ans += len_D**i    
            
        print(ans)
        for i in range(0,len_N):
            ## 遍历d 进制的数字
            keep = False
            for d in D:
                ##如果最高位小于 N 第一，
                if d < s[i]:
                    ans += len_D**(len_N - i - 1) ## 余下数位任意加
                elif d == s[i]:
                    keep = True
            if not keep:
                return ans 
                
        return ans + 1
            
        
```

