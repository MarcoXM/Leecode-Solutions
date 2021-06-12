# biweekly-contest 54

1893. Check if All the Integers in a Range Are Covered

> 给你一个二维整数数组 `ranges` 和两个整数 `left` 和 `right` 。每个 `ranges[i] = [starti, endi]` 表示一个从 `starti` 到 `endi` 的 **闭区间** 。
>
> 如果闭区间 `[left, right]` 内每个整数都被 `ranges` 中 **至少一个** 区间覆盖，那么请你返回 `true` ，否则返回 `false` 。
>
> 已知区间 `ranges[i] = [starti, endi]` ，如果整数 `x` 满足 `starti <= x <= endi` ，那么我们称整数`x` 被覆盖了。
>
> **示例 1：**
>
> ```text
> 输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
> 输出：true
> 解释：2 到 5 的每个整数都被覆盖了：
> - 2 被第一个区间覆盖。
> - 3 和 4 被第二个区间覆盖。
> - 5 被第三个区间覆盖。
> ```
>
> **示例 2：**
>
> ```text
> 输入：ranges = [[1,10],[10,20]], left = 21, right = 21
> 输出：false
> 解释：21 没有被任何一个区间覆盖。
> ```
>
> **提示：**
>
> * `1 <= ranges.length <= 50`
> * `1 <= starti <= endi <= 50`
> * `1 <= left <= right <= 50`

```python
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        visited = {}
        for x, y in ranges:
            for d in range(x , y + 1):
                visited[d] = 1
                
        for d in range(left, right + 1):
            if d not in visited:
                return False
            
        return True
```

1894. Find the Student that Will Replace the Chalk

> 一个班级里有 `n` 个学生，编号为 `0` 到 `n - 1` 。每个学生会依次回答问题，编号为 `0` 的学生先回答，然后是编号为 `1` 的学生，以此类推，直到编号为 `n - 1` 的学生，然后老师会重复这个过程，重新从编号为 `0` 的学生开始回答问题。
>
> 给你一个长度为 `n` 且下标从 `0` 开始的整数数组 `chalk` 和一个整数 `k` 。一开始粉笔盒里总共有 `k` 支粉笔。当编号为 `i` 的学生回答问题时，他会消耗 `chalk[i]` 支粉笔。如果剩余粉笔数量 **严格小于** `chalk[i]` ，那么学生 `i` 需要 **补充** 粉笔。
>
> 请你返回需要 **补充** 粉笔的学生 **编号** 。
>
> **示例 1：**
>
> ```text
> 输入：chalk = [5,1,5], k = 22
> 输出：0
> 解释：学生消耗粉笔情况如下：
> - 编号为 0 的学生使用 5 支粉笔，然后 k = 17 。
> - 编号为 1 的学生使用 1 支粉笔，然后 k = 16 。
> - 编号为 2 的学生使用 5 支粉笔，然后 k = 11 。
> - 编号为 0 的学生使用 5 支粉笔，然后 k = 6 。
> - 编号为 1 的学生使用 1 支粉笔，然后 k = 5 。
> - 编号为 2 的学生使用 5 支粉笔，然后 k = 0 。
> 编号为 0 的学生没有足够的粉笔，所以他需要补充粉笔。
> ```
>
> **示例 2：**
>
> ```text
> 输入：chalk = [3,4,1,2], k = 25
> 输出：1
> 解释：学生消耗粉笔情况如下：
> - 编号为 0 的学生使用 3 支粉笔，然后 k = 22 。
> - 编号为 1 的学生使用 4 支粉笔，然后 k = 18 。
> - 编号为 2 的学生使用 1 支粉笔，然后 k = 17 。
> - 编号为 3 的学生使用 2 支粉笔，然后 k = 15 。
> - 编号为 0 的学生使用 3 支粉笔，然后 k = 12 。
> - 编号为 1 的学生使用 4 支粉笔，然后 k = 8 。
> - 编号为 2 的学生使用 1 支粉笔，然后 k = 7 。
> - 编号为 3 的学生使用 2 支粉笔，然后 k = 5 。
> - 编号为 0 的学生使用 3 支粉笔，然后 k = 2 。
> 编号为 1 的学生没有足够的粉笔，所以他需要补充粉笔。
> ```
>
> **提示：**
>
> * `chalk.length == n`
> * `1 <= n <= 105`
> * `1 <= chalk[i] <= 105`
> * `1 <= k <= 109`

```python
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        idx = 0
        total = sum(chalk)
        k = k % total
        n = len(chalk)
        while k >= 0 :
            if k < chalk[idx % n]:
                return idx % n
            k -= chalk[idx % n]
            idx += 1
            
        
           
            
            
```



1895. Largest Magic Square

> 一个 `k x k` 的 **幻方** 指的是一个 `k x k` 填满整数的方格阵，且每一行、每一列以及两条对角线的和 **全部相等** 。幻方中的整数 **不需要互不相同** 。显然，每个 `1 x 1` 的方格都是一个幻方。
>
> 给你一个 `m x n` 的整数矩阵 `grid` ，请你返回矩阵中 **最大幻方** 的 **尺寸** （即边长 `k`）。
>
> **示例 1：**![](https://assets.leetcode.com/uploads/2021/05/29/magicsquare-grid.jpg)
>
> ```text
> 输入：grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
> 输出：3
> 解释：最大幻方尺寸为 3 。
> 每一行，每一列以及两条对角线的和都等于 12 。
> - 每一行的和：5+1+6 = 5+4+3 = 2+7+3 = 12
> - 每一列的和：5+5+2 = 1+4+7 = 6+3+3 = 12
> - 对角线的和：5+4+3 = 6+4+2 = 12
> ```
>
> **示例 2：**![](https://assets.leetcode.com/uploads/2021/05/29/magicsquare2-grid.jpg)
>
> ```text
> 输入：grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
> 输出：2
> ```
>
> **提示：**
>
> * `m == grid.length`
> * `n == grid[i].length`
> * `1 <= m, n <= 50`
> * `1 <= grid[i][j] <= 106`

```python
class Solution:
    def largestMagicSquare(self, g: List[List[int]]) -> int:
        
        s1 = [[0] * 55 for _ in range(55)]
        s2 = [[0] * 55 for _ in range(55)]
        ver = [[0] * 55 for _ in range(55)]
        hor = [[0] * 55 for _ in range(55)]
        n = len(g)
        m = len(g[0])
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                
                s1[i][j] = s1[i- 1][j-1] + g[i- 1][j-1]
            for j in range(m , 0 , - 1):
                s2[i][j] = s2[i- 1][j+ 1] + g[i- 1][j-1]
                
        for i in range(1,n + 1):
            for j in range(1, m + 1):
                ver[i][j] = ver[i][j - 1] + g[i- 1][j-1]
                hor[i][j] = hor[i - 1][j] + g[i- 1][j-1]

        
        def check(i,j,k):
            a = s1[i + k][j + k] - s1[i][j]
            b = s2[i + k][j + 1] - s2[i][j + k + 1] 
            if a == b:
                for l in range(0,k):
                    if a != ver[i+ l + 1][j + k] - ver[i+ l + 1][j]:
                        return False
                        
                    if a != hor[i + k][j + l + 1] - hor[i][j + l + 1]:
                        return False
                return True
            else:
                return False
            
        
        for k in range(min(n,m), 0, - 1):
            for i in range(n - k + 1):
                for j in range(m - k + 1):   
                    if check(i, j, k):
                        return k
                    
        return 1
```



1896. Minimum Cost to Change the Final Value of Expression

> 给你一个 **有效的** 布尔表达式，用字符串 `expression` 表示。这个字符串包含字符 `'1'`，`'0'`，`'&'`（按位 **与** 运算），`'|'`（按位 **或** 运算），`'('` 和 `')'` 。
>
> * 比方说，`"()1|1"` 和 `"(1)&()"` **不是有效** 布尔表达式。而 `"1"`， `"(((1))|(0))"` 和 `"1|(0&(1))"` 是 **有效** 布尔表达式。
>
> 你的目标是将布尔表达式的 **值** **反转** （也就是将 `0` 变为 `1` ，或者将 `1` 变为 `0`），请你返回达成目标需要的 **最少操作** 次数。
>
> * 比方说，如果表达式 `expression = "1|1|(0&0)&1"` ，它的 **值** 为 `1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 1&1 = 1` 。我们想要执行操作将 **新的** 表达式的值变成 `0` 。
>
> 可执行的 **操作** 如下：
>
> * 将一个 `'1'` 变成一个 `'0'` 。
> * 将一个 `'0'` 变成一个 `'1'` 。
> * 将一个 `'&'` 变成一个 `'|'` 。
> * 将一个 `'|'` 变成一个 `'&'` 。
>
> **注意：**`'&'` 的 **运算优先级** 与 `'|'` **相同** 。计算表达式时，括号优先级 **最高** ，然后按照 **从左到右** 的顺序运算。
>
> **示例 1：**
>
> ```text
> 输入：expression = "1&(0|1)"
> 输出：1
> 解释：我们可以将 "1&(0|1)" 变成 "1&(0&1)" ，执行的操作为将一个 '|' 变成一个 '&' ，执行了 1 次操作。
> 新表达式的值为 0 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：expression = "(0&0)&(0&0&0)"
> 输出：3
> 解释：我们可以将 "(0&0)&(0&0&0)" 变成 "(0|1)|(0&0&0)" ，执行了 3 次操作。
> 新表达式的值为 1 。
> ```
>
> **示例 3：**
>
> ```text
> 输入：expression = "(0|(1|0&1))"
> 输出：1
> 解释：我们可以将 "(0|(1|0&1))" 变成 "(0|(0|0&1))" ，执行了 1 次操作。
> 新表达式的值为 0 。
> ```
>
> **提示：**
>
> * `1 <= expression.length <= 105`
> * `expression` 只包含 `'1'`，`'0'`，`'&'`，`'|'`，`'('` 和 `')'`
> * 所有括号都有与之匹配的对应括号。
> * 不会有空的括号（也就是说 `"()"` 不是 `expression` 的子字符串）。

```python
class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        
        nums = []
        op = []
    
        def evalute():
            a = nums.pop()
            b = nums.pop()
            c = op.pop()
            
            if c == "&":
                s0 = [a[0] + b[0] , a[1] + b[0], a[0] + b[1], a[0] + b[0] + 1]
                s1 = [a[1] + b[1], a[1] + b[0] + 1, a[0]+ b[1] + 1, a[1] + a[1] + 1]
                nums.append((min(s0),min(s1)))
            else:
                s0 = [a[0] + b[0] , a[1] + b[0] + 1, a[0] + b[1] + 1, a[0] + b[0] + 1]
                s1 = [a[1] + b[1], a[1] + b[0], a[0]+ b[1], a[1] + a[1] + 1]
                nums.append((min(s0),min(s1)))
        
        for c in expression:
            if c.isdigit():
                if c == '0':
                    nums.append((0, 1))
                else:
                    nums.append((1,0))
            elif c == '(':
                op.append(c)
            elif c == ")":
                while op[-1] != '(':
                    evalute()
                op.pop()
            else:
                while op and op[-1] != '(':
                    evalute()
                op.append(c)
        while op:
            evalute()
        return max(nums[-1])
    
                    
```



