# 1101. 献给阿尔吉侬的花束



阿尔吉侬是一只聪明又慵懒的小白鼠，它最擅长的就是走各种各样的迷宫。

今天它要挑战一个非常大的迷宫，研究员们为了鼓励阿尔吉侬尽快到达终点，就在终点放了一块阿尔吉侬最喜欢的奶酪。

现在研究员们想知道，如果阿尔吉侬足够聪明，它最少需要多少时间就能吃到奶酪。

迷宫用一个 R×CR×C 的字符矩阵来表示。

字符 S 表示阿尔吉侬所在的位置，字符 E 表示奶酪所在的位置，字符 \# 表示墙壁，字符 . 表示可以通行。

阿尔吉侬在 1 个单位时间内可以从当前的位置走到它上下左右四个方向上的任意一个位置，但不能走出地图边界。

**输入格式**

第一行是一个正整数 TT，表示一共有 TT 组数据。

每一组数据的第一行包含了两个用空格分开的正整数 RR 和 CC，表示地图是一个 R×CR×C 的矩阵。

接下来的 RR 行描述了地图的具体内容，每一行包含了 CC 个字符。字符含义如题目描述中所述。保证有且仅有一个 S 和 E。

**输出格式**

对于每一组数据，输出阿尔吉侬吃到奶酪的最少单位时间。

若阿尔吉侬无法吃到奶酪，则输出“oop!”（只输出引号里面的内容，不输出引号）。

每组数据的输出结果占一行。

**数据范围**

1&lt;T≤101&lt;T≤10,  
2≤R,C≤2002≤R,C≤200

**输入样例：**

```text
3
3 4
.S..
###.
..E.
3 4
.S..
.E..
....
3 4
.S..
####
..E.
```

**输出样例：**

```text
5
1
oop!
```

```go
package main 

import (
    "fmt"
    )

type point struct {
    X, Y int
}
    
    
var g = make([][]rune, 210)
    
var dirs = [][2]int{[2]int{1, 0},[2]int{0, 1}, [2]int{-1, 0},[2]int{0, -1}}
    
func main(){
    var t int
    fmt.Scanf("%d", &t)
    for i := 0 ; i < t ; i ++ {
        var n , m int
        var s , e point
        fmt.Scanf("%d %d", &n , &m)
        var visited  = make([][]int, n)
        for j := 0 ; j < n ; j ++ {
            var tmp string
            fmt.Scanf("%s", &tmp)
            g[j] = []rune(tmp)
            visited[j] = make([]int, m)
            for k := 0 ; k < m ; k ++ {
                if g[j][k] == 'S' {
                    s.X = j
                    s.Y = k
                }
                if g[j][k] == 'E' {
                    e.X = j
                    e.Y = k
                }
                visited[j][k] = -1
            }
        }
        // fmt.Println(g)
        q := make([]point,0)
        q = append(q, s)
        visited[s.X][s.Y] = 0
        var find bool
        for len(q) > 0 {
            p  := q[0]
            q = q[1:]
            if p.X == e.X && p.Y == e.Y {
                fmt.Println(visited[p.X][p.Y])
                find = true
            }
            for _,v := range dirs {
                x := p.X + v[0]
                y := p.Y + v[1]
                if x < 0 || x >= n ||y < 0 || y >= m {
                    continue
                }
                if visited[x][y] != -1 || g[x][y] == '#'{
                    continue
                }
                visited[x][y] = visited[p.X][p.Y] + 1
                q = append(q, point{X:x, Y:y})
            }
        }
        if !find{
            fmt.Println("oop!")
        }
    }
    
}
```

