# 剑指 Offer 05. 替换空格

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if s[i] == " ":
                ans.append("%20")
            else:
                ans.append(s[i])
        
        return "".join(ans)
        
        ## or return s.replace(" ", "%20")
        
```

