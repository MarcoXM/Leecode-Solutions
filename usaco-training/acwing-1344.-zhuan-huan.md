# 1344. 转换

```go
package main

import (
    "fmt"
    )


func mirror(m [][]byte){
    N := len(m)
    for i:= 0 ; i < N ; i ++ {
        j := 0
        k := N - 1
        for j < k  {
            m[i][j],m[i][k] = m[i][k],m[i][j]
            j ++
            k -- 
        }
    }
}

func rotate(m [][]byte) {
    N := len(m)
    for i:= 0 ; i < N ; i ++ {
        for j := 0 ; j < i ; j ++ {
            m[i][j],m[j][i] = m[j][i],m[i][j]
        }
    }
    mirror(m)
}

func check_state(a , b [][]byte) (int) {

    tmp := copy_new_m(a)
    idx := 0
    for i:= 1 ; i <= 3; i ++ {
        rotate(tmp)
        if Equal(tmp,b){
            idx = i
            return idx
        }
    }
    tmp = copy_new_m(a)
    mirror(tmp)
    if Equal(tmp,b) {
        return 4
    }
    for i:= 1 ; i <= 3; i ++ {
        rotate(tmp)
        if Equal(tmp,b){ 
            return 5
        }
    }
    if Equal(a,b){ 
        return 6
    }
    return 7
}

// Equal tells whether a and b contain the same elements.
// A nil argument is equivalent to an empty slice.
func Equal(a, b [][]byte) (bool) {
    N := len(a)
    for i := 0 ; i < N ; i ++{
        for j := 0 ; j < N; j++ {
            if a[i][j] != b[i][j]{
                return false
            }
        }
    }
    return true
}

func copy_new_m (a [][]byte) ([][]byte){
    N := len(a)
    b := make([][]byte, 0)
    for i:= 0 ; i < N ; i ++ {
        tmp := make([]byte, len(a))
        copy(tmp, a[i])
        b = append(b,tmp)
    }
    return b

}

func main() {
    var N int
    fmt.Scanf("%d", &N)
    a := make([][]byte,0)
    b := make([][]byte,0)

    for i:= 0 ; i < N ; i ++ {
        var w string
        fmt.Scanf("%s",&w)
        s := []byte(w)
        a = append(a, s)
    }
    for i:= 0 ; i < N ; i ++ {
        var w string
        fmt.Scanf("%s",&w)
        s := []byte(w)
        b = append(b, s)
    }
    ans := check_state(a, b)
    fmt.Println(ans)
}

作者：王旭明
链接：https://www.acwing.com/activity/content/code/content/690401/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

