# Stack

首先,如果涉及到任何反序操作! 果斷想到stack

Recomandation of Lee215

\901. Online Stock Span

```python
class StockSpanner:

    def __init__(self):
        self.stack = []
        ## stack([prices,res])

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res
```

\[\1130. Minimum Cost Tree From Leaf Values\]\([https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O\(N\)-Time-and-Space](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O%28N%29-Time-and-Space)\)

```python
    def mctFromLeafValues(self, A):
        res = 0
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res
```

[Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C++JavaPython-Stack-Solution)

\[Online Stock Span\]\([https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O\(1](https://leetcode.com/problems/online-stock-span/discuss/168311/C++JavaPython-O%281)\)\)

\[Score of Parentheses\]\([https://leetcode.com/problems/score-of-parentheses/discuss/141777/C++JavaPython-O\(1\)-Space](https://leetcode.com/problems/score-of-parentheses/discuss/141777/C++JavaPython-O%281%29-Space)\)

[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC++Python-Loop-Twice)

