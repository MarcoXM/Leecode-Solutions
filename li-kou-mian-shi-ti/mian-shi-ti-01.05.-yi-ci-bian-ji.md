# 面试题 01.05. 一次编辑

```python
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) < len(second):
            first,second = second,first

        if len(first) - len(second) > 1:return False
        i = j = cnt = 0
        while i < len(first) and j < len(second):
            if first[i] != second[j] :
                cnt += 1
                if len(first) == len(second):
                     j += 1
                i += 1
            else:
                i += 1
                j += 1
            # print(i,j,len(first) == len(second))
            if cnt > 1: return False


        return True
```

