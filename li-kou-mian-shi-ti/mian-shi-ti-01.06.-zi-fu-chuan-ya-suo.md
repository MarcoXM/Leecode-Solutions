# 面试题 01.06. 字符串压缩

```python
class Solution:
    def compressString(self, S: str) -> str:
        if not S:return S

        ans = S[0]
        cnt = 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                cnt += 1
            else:
                ans += str(cnt)
                cnt = 1
                ans += S[i]

        return S if len(ans) + 1 >= len(S) else ans + str(cnt)
```

