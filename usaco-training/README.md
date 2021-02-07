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

```go
import (
    "fmt"
     "os"
    "bufio"
    )
    

## bufio -> 适合不知道长度的输入..
## 也没有查到for合适的写法
func main() {
    var num int
    var name string
    fmt.Scanf("%d", &num)
    var cnt int
    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() 
    
    
## rune 外面套int 改变为整形
func get(c rune) (int) {
    if c <= 'O'{
        return int(c - 'A')/3 + 2
    } else if c <= 'S'{
        return 7
    } else if c <= 'V'{
        return 8
    }
    return 9
}



```

```go
type dsu struct {
    f []int
    size []int
    cnt int
}

func (d *dsu) find(x int) int {
    if d.f[x]!=x {
        d.f[x] = d.find(d.f[x])
    }
    return d.f[x]
}

func (d *dsu) union(x, y int) int {
    fx,fy := d.find(x), d.find(y)
    if fx == fy {
        return d.size[fx] 
    }else{
        d.cnt -= 1
        if d.size[fx] >= d.size[fy] {
            d.size[fx] += d.size[fy]
            d.f[fy] = fx
            return d.size[fx]
        } else {
            d.size[fy]+= d.size[fx]
            d.f[fx] = fy
            return d.size[fy]
        }
    }
}
```

