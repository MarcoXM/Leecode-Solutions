# 703. 数独检查



数独是一种流行的单人游戏。

目标是用数字填充9x9矩阵，使每列，每行和所有9个非重叠的3x3子矩阵包含从1到9的所有数字。

每个9x9矩阵在游戏开始时都会有部分数字已经给出，通常有一个独特的解决方案。

![1.png](https://cdn.acwing.com/media/article/image/2019/04/18/19_165f3c0a61-1.png)

![2.png](https://cdn.acwing.com/media/article/image/2019/04/18/19_18efab2661-2.png)

给定完成的N2∗N2N2∗N2数独矩阵，你的任务是确定它是否是有效的解决方案。

有效的解决方案必须满足以下条件：

* 每行包含从1到N2N2的每个数字，每个数字一次。
* 每列包含从1到N2N2的每个数字，每个数字一次。
* 将N2∗N2N2∗N2矩阵划分为N2N2个非重叠N∗NN∗N子矩阵。 每个子矩阵包含从1到N2N2的每个数字，每个数字一次。

你无需担心问题的唯一性，只需检查给定矩阵是否是有效的解决方案即可。

**输入格式**

第一行包含整数T，表示共有T组测试数据。

每组数据第一行包含整数N。

接下来N2N2行，每行包含N2N2个数字（均不超过1000），用来描述完整的数独矩阵。

**输出格式**

每组数据输出一个结果，每个结果占一行。

结果表示为“Case \#x: y”，其中x是组别编号（从1开始），如果给定矩阵是有效方案则y是Yes，否则y是No。

**数据范围**

1≤T≤1001≤T≤100,  
3≤N≤63≤N≤6

**输入样例：**

```text
3
3
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
3
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
3
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 999 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

**输出样例：**

```text
Case #1: Yes
Case #2: No
Case #3: No
```

```go
package main 

import (
    "fmt"
    )
    
    
func check_line(g []int, r *[]bool) bool {
    for i := range g {
        if g[i] > n || g[i] <= 0  {
            return false
        }
        if (*r)[g[i]] {
            return false
        }
        (*r)[g[i]] = true
    }

    return true
}    
    
func check_matrix (g [][]int, col_set , area_set *[]map[int]bool) bool {
    
    for i:= range g {
        row := make([]bool, n + 1)
        if !check_line(g[i] , &row){
            return false
        }

        for j:= range g[i] {
            if _, ok := (*col_set)[j][g[i][j]]; ok {
                return false
            }
            (*col_set)[j][g[i][j]] = true
            
            if _, ok := (*area_set)[(i/m) *m + j /m][g[i][j]];ok {
                return false
            }
            (*area_set)[(i/m) *m + j /m ][g[i][j]] = true
            
        }

    }

    return true
    
}
    
    
func new_set(n int) ([]map[int]bool, []map[int]bool) {
    col_set := make([]map[int]bool,n)
    area_set := make([]map[int]bool,n)
    for i := 0 ; i < n ; i ++ {
        col_set[i] = make(map[int]bool)
        area_set[i] = make(map[int]bool)
    }
    return col_set, area_set
}
    
var n,m int
    
func main() {
    var t int
    fmt.Scanf("%d", &t)
    for i := 1 ; i <= t ; i ++{
        fmt.Scanf("%d", &m)
        n = m * m
        col_set, area_set := new_set(n)
        g := make([][]int, n)
        // break
        for j:= 0 ; j < n ; j ++ {
            g[j] = make([]int,n)
            for k := 0; k < n ; k ++ {
                fmt.Scanf("%d",&g[j][k])
            }
        }
        ans:= ""
        if check_matrix(g , &col_set , &area_set){
            ans += "Yes"
        }else {
            ans +="No"
        }
        fmt.Printf("Case #%d: %s\n",i , ans)

    }
    
}
```

