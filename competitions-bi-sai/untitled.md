# weekly-contest-244

1886. Determine Whether Matrix Can Be Obtained By Rotation

> 给你两个大小为 `n x n` 的二进制矩阵 `mat` 和 `target` 。现 **以 90 度顺时针轮转** 矩阵 `mat` 中的元素 **若干次** ，如果能够使 `mat` 与 `target` 一致，返回 `true` ；否则，返回 __`false` _。_
>
> **示例 1：**![](https://assets.leetcode.com/uploads/2021/05/20/grid3.png)
>
> ```text
> 输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
> 输出：true
> 解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。
> ```
>
> **示例 2：**![](https://assets.leetcode.com/uploads/2021/05/20/grid4.png)
>
> ```text
> 输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
> 输出：false
> 解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。
> ```
>
> **示例 3：**![](https://assets.leetcode.com/uploads/2021/05/26/grid4.png)
>
> ```text
> 输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
> 输出：true
> 解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。
> ```
>
> **提示：**
>
> * `n == mat.length == target.length`
> * `n == mat[i].length == target[i].length`
> * `1 <= n <= 10`
> * `mat[i][j]` 和 `target[i][j]` 不是 `0` 就是 `1`

```python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        for i in range(4):
            mat = self.rotate(mat)
            if target == mat :
                return True
            
        return False
        
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        return matrix_new


```

1887. Reduction Operations to Make the Array Elements Equal

> 给你一个整数数组 `nums` ，你的目标是令 `nums` 中的所有元素相等。完成一次减少操作需要遵照下面的几个步骤：
>
> 1. 找出 `nums` 中的 **最大** 值。记这个值为 `largest` 并取其下标 `i` （**下标从 0 开始计数**）。如果有多个元素都是最大值，则取最小的 `i` 。
> 2. 找出 `nums` 中的 **下一个最大** 值，这个值 **严格小于** `largest` ，记为 `nextLargest` 。
> 3. 将 `nums[i]` 减少到 `nextLargest` 。
>
> 返回使 __`nums` __中的所有元素相等的操作次数。
>
> **示例 1：**
>
> ```text
> 输入：nums = [5,1,3]
> 输出：3
> 解释：需要 3 次操作使 nums 中的所有元素相等：
> 1. largest = 5 下标为 0 。nextLargest = 3 。将 nums[0] 减少到 3 。nums = [3,1,3] 。
> 2. largest = 3 下标为 0 。nextLargest = 1 。将 nums[0] 减少到 1 。nums = [1,1,3] 。
> 3. largest = 3 下标为 2 。nextLargest = 1 。将 nums[2] 减少到 1 。nums = [1,1,1] 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：nums = [1,1,1]
> 输出：0
> 解释：nums 中的所有元素已经是相等的。
> ```
>
> **示例 3：**
>
> ```text
> 输入：nums = [1,1,2,2,3]
> 输出：4
> 解释：需要 4 次操作使 nums 中的所有元素相等：
> 1. largest = 3 下标为 4 。nextLargest = 2 。将 nums[4] 减少到 2 。nums = [1,1,2,2,2] 。
> 2. largest = 2 下标为 2 。nextLargest = 1 。将 nums[2] 减少到 1 。nums = [1,1,1,2,2] 。 
> 3. largest = 2 下标为 3 。nextLargest = 1 。将 nums[3] 减少到 1 。nums = [1,1,1,1,2] 。 
> 4. largest = 2 下标为 4 。nextLargest = 1 。将 nums[4] 减少到 1 。nums = [1,1,1,1,1] 。
> ```
>
> **提示：**
>
> * `1 <= nums.length <= 5 * 104`
> * `1 <= nums[i] <= 5 * 104`

```python
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        ss = sorted(list(set(nums)))
        cnt = {k:v for v,k in enumerate(ss)}
        
        ans = 0
        for n in nums:
            ans += cnt[n]
        
        return ans
```



1888. Minimum Number of Flips to Make the Binary String Alternating

> 给你一个二进制字符串 `s` 。你可以按任意顺序执行以下两种操作任意次：
>
> * **类型 1 ：删除** 字符串 `s` 的第一个字符并将它 **添加** 到字符串结尾。
> * **类型 2 ：选择** 字符串 `s` 中任意一个字符并将该字符 **反转** ，也就是如果值为 `'0'` ，则反转得到 `'1'` ，反之亦然。
>
> 请你返回使 `s` 变成 **交替** 字符串的前提下， **类型 2** 的 **最少** 操作次数 。
>
> 我们称一个字符串是 **交替** 的，需要满足任意相邻字符都不同。
>
> * 比方说，字符串 `"010"` 和 `"1010"` 都是交替的，但是字符串 `"0100"` 不是。
>
> **示例 1：**
>
> ```text
> 输入：s = "111000"
> 输出：2
> 解释：执行第一种操作两次，得到 s = "100011" 。
> 然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：s = "010"
> 输出：0
> 解释：字符串已经是交替的。
> ```
>
> **示例 3：**
>
> ```text
> 输入：s = "1110"
> 输出：1
> 解释：对第二个字符执行第二种操作，得到 s = "1010" 。
> ```
>
> **提示：**
>
> * `1 <= s.length <= 105`
> * `s[i]` 要么是 `'0'` ，要么是 `'1'` 。

{% tabs %}
{% tab title="Python" %}
```python
### 前后缀分解,枚举每个分界点的值　

class Solution:
    def minFlips(self, s: str) -> int:
        ## 预处理 
        n = len(s)
        l = [[0] * n for _ in range(2)]
        r = [[0] * n for _ in range(2)]
        
        for i in range(2):
            c = 0
            k = i
            for j in range(n):
                if k != ord(s[j]) - ord("0"): c += 1
                l[i][j] = c
                k ^= 1
                
        for i in range(2):
            c = 0
            k = i
            for j in range(n - 1, - 1, - 1):
                if k != ord(s[j]) - ord("0"): c += 1
                r[i][j] = c
                k ^= 1
            
        if n % 2 == 0 :
            return min(l[0][n-1],l[1][n - 1])
        
        else:
            res = min(l[0][n-1],l[1][n - 1])
            for i in range(n - 1):
                res = min(res, l[0][i] + r[1][i + 1],l[1][i] + r[0][i + 1])
                
            return res
```
{% endtab %}
{% endtabs %}

1889.  Minimum Space Wasted From Packaging

> 给你 `n` 个包裹，你需要把它们装在箱子里，**每个箱子装一个包裹**。总共有 `m` 个供应商提供 **不同尺寸** 的箱子（每个规格都有无数个箱子）。如果一个包裹的尺寸 **小于等于** 一个箱子的尺寸，那么这个包裹就可以放入这个箱子之中。
>
> 包裹的尺寸用一个整数数组 `packages` 表示，其中 `packages[i]` 是第 `i` 个包裹的尺寸。供应商用二维数组 `boxes` 表示，其中 `boxes[j]` 是第 `j` 个供应商提供的所有箱子尺寸的数组。
>
> 你想要选择 **一个供应商** 并只使用该供应商提供的箱子，使得 **总浪费空间最小** 。对于每个装了包裹的箱子，我们定义 **浪费的** 空间等于 `箱子的尺寸 - 包裹的尺寸` 。**总浪费空间** 为 **所有** 箱子中浪费空间的总和。
>
> * 比方说，如果你想要用尺寸数组为 `[4,8]` 的箱子装下尺寸为 `[2,3,5]` 的包裹，你可以将尺寸为 `2` 和 `3` 的两个包裹装入两个尺寸为 `4` 的箱子中，同时把尺寸为 `5` 的包裹装入尺寸为 `8` 的箱子中。总浪费空间为 `(4-2) + (4-3) + (8-5) = 6` 。
>
> 请你选择 **最优** 箱子供应商，使得 **总浪费空间最小** 。如果 **无法** 将所有包裹放入箱子中，请你返回 `-1` 。由于答案可能会 **很大** ，请返回它对 ****`109 + 7` **取余** 的结果。
>
> **示例 1：**
>
> ```text
> 输入：packages = [2,3,5], boxes = [[4,8],[2,8]]
> 输出：6
> 解释：选择第一个供应商最优，用两个尺寸为 4 的箱子和一个尺寸为 8 的箱子。
> 总浪费空间为 (4-2) + (4-3) + (8-5) = 6 。
> ```
>
> **示例 2：**
>
> ```text
> 输入：packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]
> 输出：-1
> 解释：没有箱子能装下尺寸为 5 的包裹。
> ```
>
> **示例 3：**
>
> ```text
> 输入：packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]
> 输出：9
> 解释：选择第三个供应商最优，用两个尺寸为 5 的箱子，两个尺寸为 10 的箱子和两个尺寸为 14 的箱子。
> 总浪费空间为 (5-3) + (5-5) + (10-8) + (10-10) + (14-11) + (14-12) = 9 。
> ```
>
> **提示：**
>
> * `n == packages.length`
> * `m == boxes.length`
> * `1 <= n <= 105`
> * `1 <= m <= 105`
> * `1 <= packages[i] <= 105`
> * `1 <= boxes[j].length <= 105`
> * `1 <= boxes[j][k] <= 105`
> * `sum(boxes[j].length) <= 105`
> * `boxes[j]` 中的元素 **互不相同** 。

{% tabs %}
{% tab title="python" %}
```python
class Solution:
    def minWastedSpace(self, a: List[int], bs: List[List[int]]) -> int:
        a.sort()
        mod = 10 ** 9 + 7
        s = sum(a)
        n = len(a)
        res = float("inf")
        for b in bs:
            b.sort()
            if b[-1] < a[-1]:continue
            
            lidx = -1
            tmp = -s
            for x in b:
                l = last
                r = n - 1
                while l < r :
                    mid = l + r + 1 >> 1
                    if a[mid] > x: 
                        r = mid - 1
                    else :
                        l = mid
                if r == last :continue
                tmp += (r - last) * x
                last = r 
            res = min(res,tmp)
        if res == float("inf"):retunrn -1
        return res %mod 
        



```
{% endtab %}

{% tab title="Python 暴力异步 不行" %}
```python
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        
        mod = 10 ** 9 + 7
        
        import asyncio
        packages.sort()


        async def check(bs, packages):
            tmp = []
            bs.sort()
            i = 0
            j = 0
            ans = 0
            while i < len(packages):
                while i < len(packages) and j < len(bs) and packages[i] <= bs[j]:
                    ans += bs[j] - packages[i]
                    i += 1
                j += 1
                if i < len(packages) and j >= len(bs):
                    return -1
            # print(ans)
            return ans

        self.run_time = float("inf")
        async def main(): # coroutine
            # global run_time
            # await sleeper(1, i=0)
            tasks = []
            for i, bs in enumerate(boxes):
                tasks.append(
                    asyncio.create_task(
                        check(bs, packages)
                    )
                )

            ## append task and packed by async
            results = await asyncio.gather(*tasks)
            for run_time_result in results:
                if run_time_result != -1:
                    self.run_time = min(run_time_result,self.run_time)

            # main()
        asyncio.run(main()) 


        return self.run_time % mod  if self.run_time != float("inf") else -1
```
{% endtab %}
{% endtabs %}







