# 449. 质因数分解



已知正整数n是两个不同的质数的乘积，试求出较大的那个质数。

**输入格式**

输入只有一行，包含一个正整数n。

**输出格式**

输出只有一行，包含一个正整数p，即较大的那个质数。

**数据范围**

6≤n≤2∗1096≤n≤2∗109

**输入样例：**

```text
21
```

**输出样例：**

```text
7
```

```go
package main

import (
    "fmt"
    )
    
func main(){
    var n int
    fmt.Scanf("%d",&n)
    
    for i :=2 ; i * i <= n ; i ++ {
        if n %i == 0 {
            fmt.Println(n/i)
            break
            
        }
    }
}
```

