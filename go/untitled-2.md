# 445. 数字反转



给定一个整数，请将该数各个位上数字反转得到一个新数。

新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零。

**输入格式**

输入共1行，1个整数N。

**输出格式**

输出共1行，1个整数表示反转后的新数。

**数据范围**

\|N\|≤109\|N\|≤109

**输入样例：**

```text
123
```

**输出样例：**

```text
321
```

**输入样例：**

```text
-380
```

**输出样例：**

```text
-83
```

```go
package main 

import (
    "fmt"
    )
    
func check(n int) int {
    ans := 0 
    for n > 0 {
        ans =  (n % 10) + ans * 10
        n /= 10
    }
    return ans
}
    
func main(){
    var n int 
    fmt.Scanf("%d" , &n)
    ans := 0
    if n < 0 {
        ans = - check(-n)
    }else {
        ans = check(n)
    }

    fmt.Println(ans)
    
}
```

