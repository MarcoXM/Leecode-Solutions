# 1591. Strange Printer II

```python
class Solution:
    def isPrintable(self, A):
        m, n = len(A), len(A[0])
        pos = [[m, n, 0, 0] for i in range(61)]
        colors = set()
        for i in range(m):
            for j in range(n):
                c = A[i][j]
                colors.add(c)
                pos[c][0] = min(pos[c][0], i)
                pos[c][1] = min(pos[c][1], j)
                pos[c][2] = max(pos[c][2], i)
                pos[c][3] = max(pos[c][3], j)

        def test(c):
            for i in range(pos[c][0], pos[c][2] + 1):
                for j in range(pos[c][1], pos[c][3] + 1):
                    if A[i][j] > 0 and A[i][j] != c:
                        return False
            for i in range(pos[c][0], pos[c][2] + 1):
                for j in range(pos[c][1], pos[c][3] + 1):
                    A[i][j] = 0
            return True

        while colors:
            colors2 = set()
            for c in colors:
                if not test(c):
                    colors2.add(c)
            if len(colors2) == len(colors):
                return False
            colors = colors2
        return True
```

