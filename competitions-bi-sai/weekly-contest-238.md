# weekly-contest-238



1387. Sum of Digits in Base K

```python
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        res = 0
        while n :
            res += n % k
            n //= k
            
        return res
```

1388. Frequency of the Most Frequent Element

```python
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ## 前缀和， 就是太犟了， 一定用前缀和做
        nums.sort()
        pre_sum = [0]
        for i in range(len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
            
        res = 0
        def get(idx):
            l = 0 
            r = idx 
            sj = pre_sum[idx]
            while l < r :
                mid = l + r >> 1
                if nums[idx] * (idx - mid) - (sj - pre_sum[mid]) > k:
                    l = mid + 1
                else:
                    r = mid
            
            return idx - l + 1
        
        res = 0
        for i in range(len(nums)):
            res = max(res, get(i))
        return res
        
```



1389. Longest Substring Of All Vowels in Order

```python
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        
## 这题话好多时间， 看着以为是子序列问题。
        tmp = word + "0"
        nums = []
        cnt = 1
        for i in range(1,len(tmp)):
            if tmp[i] == tmp[i-1]:
                cnt += 1
            else:
                nums.append((tmp[i - 1], cnt))
                cnt = 1
        
        ans = 0
        for i in range(len(nums) - 4):
            if nums[i][0] == "a":
                if nums[i + 1][0] == "e":
                    if nums[i + 2][0] == "i":
                        if nums[i + 3][0] == "o":
                            if nums[i + 4][0] == "u":
                                ans = max(ans, nums[i][1] + nums[i + 1][1] + nums[i + 2][1] + nums[i + 3][1] + nums[i + 4][1])
        return ans
                
```

1840. Maximum Building Height

```python
class Solution:
    def maxBuilding(self, n: int, h: List[List[int]]) -> int:
    
    
## 线性规划问题 
        h = h + [[1,0]]
        h = sorted(h,key = lambda x :x[0])
        if h[-1][0] != n :
            h.append([n, n - 1])

        m = len(h)
        f = [float("inf")] * (m + 1)
        g = [float("inf")] * (m + 1)

        f[0] = -1 
        for i in range(1, m):
            x, y  = h[i]
            f[i] = min(f[i - 1], y - x)

        for i in range(m - 1, - 1, - 1):
            x , y = h[i]
            g[i] = min(g[i + 1], y + x)


        res = 0
        for i in range(m):
            x = h[i][0]
            if i :
                Y = (f[i - 1]+ g[i] )//2
                X = Y - f[i - 1]
                if X >= h[i - 1][0] and X <=h[i][0]:
                    res = max(res, Y)
            res = max(res, min(x + f[i], -x + g[i]))

        return res
```

总结好可惜， 争取变回绿牌吧 ！

