# USACO Training

挖新的坑永远是最爽的

前言：Leetcode 使用得太久了，其他要自己处理输入的平台一开始还使用不习惯

```python
Python

## 这时是string,再根据情况转换 
data = input() ## string
```



```cpp
C++

#include <iostream>
using namespace std;

int main() {
    int data;
    cin << data ;
   //先定义变量，再赋值
}
```



```go
Golang

package main

import (
  "fmt"
)

func main(){
  var data int
  fmt.Scanf("%s", &A)
  
  //定义变量，赋值指针
}

```

> `Rune`是Go语言里面的字符类型，可以当做是C/C++里面的`char`，只不过`Rune`是UTF-8编码的，本质是`int32`的别名。

```go

//Go sort slices of slices, 要descend 就修改less

type Element [][]int

func (p Element) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p Element) Len() int           { return len(p) }
func (p Element) Less(i, j int) bool {
    if p[i][0] != p[j][0] {
        return p[i][0] < p[j][0] 
    } else {
        return p[i][1] < p[j][1]
    }
}
```

