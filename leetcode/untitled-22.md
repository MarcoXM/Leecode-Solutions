# 1706. Where Will the Ball Fall

```python
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def check(i,j):
            while i < len(grid):
                
                if grid[i][j] == 1:
                    if j + 1 < len(grid[0]):
                        if grid[i][j + 1] == -1:
                            return -1
                        else:
                            i += 1
                            j += 1
                    elif j + 1 == len(grid[0]) :return -1
                else:
                    if j - 1 >= 0 :
                        if grid[i][j - 1] == 1:
                            return -1
                        else:
                            i += 1
                            j -= 1
                    elif j - 1 < 0  :return -1
                    
            return j
        return [check(0, j) for j in range(len(grid[0]))]
                    
```

