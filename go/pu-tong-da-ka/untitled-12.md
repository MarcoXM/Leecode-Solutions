# 89. a^b



求 aa 的 bb 次方对 pp 取模的值。

**输入格式**

三个整数 a,b,pa,b,p ,在同一行用空格隔开。

**输出格式**

输出一个整数，表示`a^b mod p`的值。

**数据范围**

0≤a,b≤1090≤a,b≤109  
1≤p≤1091≤p≤109

**输入样例：**

```text
3 2 7
```

**输出样例：**

```text
2
```

```go
package main 

import (
    "fmt"
    )
    
    
func qmi( a, b ,c int) int {
    var res int 
    res = 1%c
    for b > 0 {
        if b % 2 == 1 {
            res = res * a % c
        } 
        a = a * a % c
        b >>= 1
    }
    return res % c
    
}
    
func main() {
    var n , m , p int
    fmt.Scanf("%d %d %d", &n, &m, &p)
    fmt.Println(qmi(n ,m , p))
}
```

