# 1773. Count Items Matching a Rule

```python
class Solution:
    def countMatches(self, items: List[List[str]], a: str, b: str) -> int:
        
        res = 0
        for i in range(len(items)):
            if a == "type" and items[i][0] == b:
                res += 1
        
            elif a == "color" and items[i][1] == b:
                res += 1
            
            elif a == "name" and items[i][2] == b:
                
                res += 1
                
        return res
                
```

