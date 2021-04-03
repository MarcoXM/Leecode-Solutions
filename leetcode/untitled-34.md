# 1812. Determine Color of a Chessboard Square

```python
class Solution:
    def squareIsWhite(self, c: str) -> bool:
        w = c[0]
        row = int(c[1]) 
        col = ord(w) - ord("a") + 1
        
        if row %2 == 0 :
            if col%2== 0 :
                return False
            else:
                return True
            
        else:
            if col%2== 0 :
                return True
            else:
                return False
```

