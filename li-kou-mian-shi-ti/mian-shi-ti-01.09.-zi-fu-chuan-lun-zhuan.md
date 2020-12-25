# 面试题 01.09. 字符串轮转

```python
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False

        return s1 in s2 + s2
```

