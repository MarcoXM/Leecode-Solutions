from typing import List



class Solution:
    def largestMagicSquare(self, g: List[List[int]]) -> int:
        
        s1 = [[0] * 55 for _ in range(55)]
        s2 = [[0] * 55 for _ in range(55)]
        ver = [[0] * 55 for _ in range(55)]
        hor = [[0] * 55 for _ in range(55)]
        n = len(g)
        m = len(g[0])
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                
                s1[i][j] = s1[i- 1][j-1] + g[i- 1][j-1]
            for j in range(m , 0 , - 1):
                s2[i][j] = s2[i- 1][j+ 1] + g[i- 1][j-1]
                
        for i in range(1,n + 1):
            for j in range(1, m + 1):
                ver[i][j] = ver[i][j - 1] + g[i- 1][j-1]
                hor[i][j] = hor[i - 1][j] + g[i- 1][j-1]

        
        def check(i,j,k):
            a = s1[i + k][j + k] - s1[i][j]
            b = s2[i + k][j + 1] - s2[i][j + k + 1] 
            if a == b:
                for l in range(0,k):
                    if a != ver[i+ l + 1][j + k] - ver[i+ l + 1][j]:
                        return False
                        
                    if a != hor[i + k][j + l + 1] - hor[i][j + l + 1]:
                        return False
                return True
            else:
                return False
            
        
        for k in range(min(n,m), 0, - 1):
            for i in range(n - k + 1):
                for j in range(m - k + 1):   
                    if check(i, j, k):
                        return k
                    
        return 1


s = Solution()

g = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
print("answer:  ",  s.largestMagicSquare(g))