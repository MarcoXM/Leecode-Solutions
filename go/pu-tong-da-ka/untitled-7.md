# 425. 明明的随机数



明明想在学校中请一些同学一起做一项问卷调查。

为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数，对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。

然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。

请你协助明明完成“去重”与“排序”的工作。

**输入格式**

输入文件包含2行，第1行为1个正整数，表示所生成的随机数的个数：N 。

第2行有N个用空格隔开的正整数，为所产生的随机数。

**输出格式**

输出文件也是2行，第1行为1个正整数M，表示不相同的随机数的个数。

第2行为M个用空格隔开的正整数，为从小到大排好序的不相同的随机数。

**数据范围**

1≤N≤1001≤N≤100

**输入样例：**

```text
10
20 40 32 67 40 20 89 300 400 15
```

**输出样例：**

```text
8
15 20 32 40 67 89 300 400
```

```go
package main

import (
    "fmt"
    "sort"
    )
    
func main(){
    var n int
    fmt.Scanf("%d", &n)
    a := make([]int,n)
    m := make(map[int]bool)
    for i := 0 ; i< n ; i ++ {
        fmt.Scanf("%d",&a[i])
        if _ , ok:= m[a[i]]; !ok{
            m[a[i]] = true
        } else {
            m[a[i]] = false
        }
    }

    keys := make([]int, 0, len(m))
    for k := range m {
    	keys = append(keys, k)
    }
    sort.Ints(keys)
    fmt.Println(len(keys))
    for _, k := range keys {
        fmt.Printf("%d ",k)
    }
    
}
```

