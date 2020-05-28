## may 26th

https://leetcode.com/problems/gray-code/

```python

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0] # 天生带零
        for i in range(n):
            addOn = 1 << i
            for j in range(len(res)-1,-1,-1):
                ## 每次把上一回的解,倒序,并在最高位+1 的位置加上1 
                res.append(res[j] + addOn)
                
        return res
            
```

```python

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0] # 天生带零
        for i in range(1, 1<<n):
            prev = res[i-1]
            if i & 1 == 1:
                curr = prev ^ 1
                res.append(curr)
            else:
                temp = prev
                for j in range(n):
                    if temp & 1 == 1 :
                        curr = prev ^ (1 << (j + 1)) ## 前一位变 1
                        res.append(curr)
                        break
                    temp = temp >> 1 # 右移动一位, 这样才能保证每次与1 比较
        return res
             
```

\535. Encode and Decode TinyURL

```python

class Codec:
    def __init__(self):
        self.dict = {}
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        key = 'http://tinyurl.com/' +  str(hash(longUrl))
        self.dict[key] = longUrl
        return key
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
```

