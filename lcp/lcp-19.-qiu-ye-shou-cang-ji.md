# LCP 19. 秋叶收藏集

> 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 leaves， 字符串 leaves 仅包含小写字符 r 和 y， 其中字符 r 表示一片红叶，字符 y 表示一片黄叶。 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
>
> 示例 1：
>
> 输入：leaves = "rrryyyrryyyrr"
>
> 输出：2
>
> 解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"
>
> 示例 2：
>
> 输入：leaves = "ryr"
>
> 输出：0
>
> 解释：已符合要求，不需要额外操作
>
> 提示：
>
> 3 &lt;= leaves.length &lt;= 10^5 leaves 中只包含字符 'r' 和字符 'y'

{% tabs %}
{% tab title="" %}
```

```
{% endtab %}

{% tab title="" %}
```

```
{% endtab %}

{% tab title="" %}
```

```
{% endtab %}

{% tab title="Go" %}
```go
func minimumOperations(leaves string) int {
    n := len(leaves)
    dp := make([][]int,n)
    for i := range dp{
        dp[i] = make([]int, 3)
    }
    dp[0][0] = bool2int(leaves[0] == 'y')
    dp[0][1] = 2 << 31
    dp[0][2] = 2 << 31
    dp[1][2] = 2 << 31
    for i:=1 ; i < n ; i ++ {
        yellow2red := bool2int(leaves[i] == 'y')
        dp[i][0] = dp[i-1][0] + yellow2red
        dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + ( 1 - yellow2red)
        if i > 1{
            dp[i][2] = min(dp[i-1][1], dp[i-1][2]) + yellow2red
        }
    }
    return dp[n-1][2]
}
func bool2int(b bool ) int {
    if b {
        return 1
    } 
    return 0
}

func min( a, b int) int{
    if a < b {
        return a
    }
    return b
}
```
{% endtab %}

{% tab title="Python" %}
```python
class Solution:
    def minimumOperations(self, leaves: str) -> int:

        ans = 0

        ## 怎么这么难呀，看不懂呀
        ## 这是dp， 这个状态有三种 0， 1， 2
        ## 所以dp 数组 n * 3 大小

        dp = [[10**9, 10**9, 10**9] for _ in range(len(leaves))]
        ## dp 是function （ idx， state） return 最小操作 
        ## r,y,r
        dp[0][0] =  1 if leaves[0] == "y" else 0
        ## inf 代表无效的 
        dp[0][1] = dp[0][2] = dp[1][2] = float("inf")

        for i in range(1,len(leaves)):
            Yellow2Red = 1 if leaves[i] =="y" else 0
            dp[i][0] = dp[i - 1][0] + Yellow2Red 
            ## 我们还是第一个r，所以如果是黄 我们就+ 1
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + (1 - Yellow2Red)
            ## 这是我们如果是yellow了，就不用改变了

            ## 保证有元素
            if i > 1:
                dp[i][2] = min(dp[i-1][2] , dp[i-1][1]) + Yellow2Red

        return dp[-1][2]
```
{% endtab %}
{% endtabs %}

