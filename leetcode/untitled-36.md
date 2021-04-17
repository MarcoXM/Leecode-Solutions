# Untitled

```python
class Solution:
    def makeStringSorted(self, s: str) -> int:
        
        mod = 10**9 + 7 
        ## 本质排列的
        f = [0] * 3010
        g = [0] * 3010
        
        def qmi (a, b ):
            res = 1
            while b :
                if b & 1:
                    res = res * a % mod
                a = a * a % mod
                b >>= 1
            
            return res
        
        f[0] = g[0] = 1
        for i in range(1, len(s) + 1):
            f[i] = f[i -1] * i % mod
            g[i] = qmi(f[i], mod - 2)
            
        ans = 0
        cnt = [0] * 26
        
        def get():
            s = 0
            for i in range(26):
                s += cnt[i]
            res= f[s]
            for i in range(26):
                res = res * g[cnt[i]]% mod
            return res
        
        
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        for c in s:
            x = ord(c) - ord("a")
            for i in range(x):
                if cnt[i] == 0 : continue
                cnt[i] -= 1
                ans = (ans + get()) % mod
                cnt[i] += 1
            cnt[x] -= 1
            
        return ans
        
        
        
```

