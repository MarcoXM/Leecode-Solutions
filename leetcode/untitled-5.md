# Untitled

```text
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s,e = rounds[0], rounds[-1]
        if e >= s:
            return list(range(s, e+1))
        else:
            return list(range(1, e+1)) + list(range(s, n+1))
```

```text
https://leetcode-cn.com/problems/detect-cycles-in-2d-grid/solution/kan-liao-ren-jia-de-da-an-jia-shang-liao-bing-cha-/
```

