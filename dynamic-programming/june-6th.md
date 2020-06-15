## june 6th

\836. Rectangle Overlap

````python

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ## 首先还是明确定义
        ## 什么是overlap 
        
        ## 反例 我小的比你大的大, 大的比你小的小,
        ## 一开始找正例,case 多 
        if (rec1[0]>=rec2[2]) or (rec1[2]<=rec2[0]) or (rec1[3]<=rec2[1]) or (rec1[1]>=rec2[3]):
            return False
        else:
            return True
````

\682. Baseball Game

```python
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ##　"C" 
        ## 读题以后　天生stack
        ans = 0
        stack = []
        for p in ops:
            if p == "C":
                ans -= stack[-1]
                stack.pop()
            elif p == "D":
                ans += stack[-1]*2
                stack.append(stack[-1]*2)
            elif p == "+":
                ans += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(p))
                ans += int(p) 
        ## 这就是数据处理题....
        return ans 
```

