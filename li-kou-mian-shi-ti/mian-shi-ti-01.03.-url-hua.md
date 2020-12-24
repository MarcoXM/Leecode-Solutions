# 面试题 01.03. URL化

```python
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ","%20")
```

