## may-21th

\1332. Number of 1 Bits

```python

class Solution:
    """
    @param n: an unsigned integer
    @return: the number of ’1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        
        ### 判定 bin(末位) & 1 是否爲真
        c = 0
        while n >= 1 :
            if n & 1:
                c += 1
            n = n >> 1
            
        return c
```



\844. Number Pair Statistics

```python

class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    ## 暴力超時
    def pairNumbers(self, p):
        # Write your code here
        c = 0
        ## 服了 這些point 是struct 
        for i in range(len(p)):
            for j in range(i + 1,len(p)):
                if ((p[i].x + p[j].x) & 1) and ((p[i].y + p[j].y) & 1) :
                    continue
                c += 1 
        return c
```

```python
class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    def pairNumbers(self, p):
        # Write your code here
        binp = [0] * 4 
        for i in range(len(p)):
            if p[i].x & 1 == 1:
                if p[i].y & 1 == 1:
                    binp[3] += 1
                else:
                    binp[2] += 1
                    
            elif p[i].x & 1 == 0:
                if p[i].y & 1 == 1:
                    binp[1] += 1
                else:
                    binp[0] += 1

        return sum(map(lambda x : (x*(x-1))//2,binp))
        
```

