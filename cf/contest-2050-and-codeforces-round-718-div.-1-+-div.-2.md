# Contest 2050 and Codeforces Round \#718 \(Div. 1 + Div. 2\)

这次考的是贪心和构造，确实不太会

A. Sum of 2050time limit per test1 secondmemory limit per test256 megabytesinputstandard inputoutputstandard output

A number is called 2050-number if it is 20502050, 2050020500, ..., \(2050⋅10𝑘2050⋅10k for integer 𝑘≥0k≥0\).

Given a number 𝑛n, you are asked to represent 𝑛n as the sum of some \(not necessarily distinct\) 2050-numbers. Compute the minimum number of 2050-numbers required for that.Input

The first line contains a single integer 𝑇T \(1≤𝑇≤10001≤T≤1000\) denoting the number of test cases.

The only line of each test case contains a single integer 𝑛n \(1≤𝑛≤10181≤n≤1018\) denoting the number to be represented.Output

For each test case, output the minimum number of 2050-numbers in one line.

If 𝑛n cannot be represented as the sum of 2050-numbers, output −1−1 instead.  
  


```python
t =int(input())
 
 
def get(n):
    res = 0
    while n:
        res += (n % 10)
        n //= 10
        
    return res 
 
for _ in range(t):
    
    n = int(input())
    if n % 2050 :
        print(-1)
        
    else:
        print(get(n//2050))
```



B. Morning Joggingtime limit per test1 secondmemory limit per test256 megabytesinputstandard inputoutputstandard output

The 2050 volunteers are organizing the "Run! Chase the Rising Sun" activity. Starting on Apr 25 at 7:30 am, runners will complete the 6km trail around the Yunqi town.

There are 𝑛+1n+1 checkpoints on the trail. They are numbered by 00, 11, ..., 𝑛n. A runner must start at checkpoint 00 and finish at checkpoint 𝑛n. No checkpoint is skippable — he must run from checkpoint 00 to checkpoint 11, then from checkpoint 11 to checkpoint 22 and so on. Look at the picture in notes section for clarification.

Between any two adjacent checkpoints, there are 𝑚m different paths to choose. For any 1≤𝑖≤𝑛1≤i≤n, to run from checkpoint 𝑖−1i−1 to checkpoint 𝑖i, a runner can choose exactly one from the 𝑚m possible paths. The length of the 𝑗j-th path between checkpoint 𝑖−1i−1 and 𝑖i is 𝑏𝑖,𝑗bi,j for any 1≤𝑗≤𝑚1≤j≤m and 1≤𝑖≤𝑛1≤i≤n.

To test the trail, we have 𝑚m runners. Each runner must run from the checkpoint 00 to the checkpoint 𝑛n once, visiting all the checkpoints. Every path between every pair of adjacent checkpoints needs to be ran by exactly one runner. If a runner chooses the path of length 𝑙𝑖li between checkpoint 𝑖−1i−1 and 𝑖i \(1≤𝑖≤𝑛1≤i≤n\), his tiredness ismin𝑖=1𝑛𝑙𝑖,mini=1nli,i. e. the minimum length of the paths he takes.

Please arrange the paths of the 𝑚m runners to minimize the sum of tiredness of them.Input

Each test contains multiple test cases. The first line contains the number of test cases 𝑡t \(1≤𝑡≤100001≤t≤10000\). Description of the test cases follows.

The first line of each test case contains two integers 𝑛n and 𝑚m \(1≤𝑛,𝑚≤1001≤n,m≤100\).

The 𝑖i-th of the next 𝑛n lines contains 𝑚m integers 𝑏𝑖,1bi,1, 𝑏𝑖,2bi,2, ..., 𝑏𝑖,𝑚bi,m \(1≤𝑏𝑖,𝑗≤1091≤bi,j≤109\).

It is guaranteed that the sum of 𝑛⋅𝑚n⋅m over all test cases does not exceed 104104.Output

For each test case, output 𝑛n lines. The 𝑗j-th number in the 𝑖i-th line should contain the length of the path that runner 𝑗j chooses to run from checkpoint 𝑖−1i−1 to checkpoint 𝑖i. There should be exactly 𝑚m integers in the 𝑖i-th line and these integers should form a permuatation of 𝑏𝑖,1bi,1, ..., 𝑏𝑖,𝑚bi,m for all 1≤𝑖≤𝑛1≤i≤n.

If there are multiple answers, print any.

```python
t =int(input())
 
 
for _ in range(t):
    
    n, m  = list(map(int,input().split()))
    data = []
    nums = []
    dit ={}
    for i in range(n):
        b = list(map(int,input().split()))
        data.append(b)
        nums += [(v, i, j)for j, v in enumerate(b)]
    
    nums.sort()
    # print(nums)
    can = nums[:m]
 
    idx = 0
    ans = [[0] * m for _ in range(n)]
    cnt = [0] * n
    for col in range(m):
        val, i , j = nums[idx] 
        ans[i][col] = val
        cnt[i] += 1
        idx+= 1
        
    for i in range(n):
        tmp = sorted(data[i])[cnt[i]:]
        idx = 0
        for j in range(m):
            if not ans[i][j]:
                ans[i][j] = tmp[idx]
                idx += 1
    
    for d in ans:
        print(*d)
```

C. Fillomino 2time limit per test1 secondmemory limit per test256 megabytesinputstandard inputoutputstandard output

Fillomino is a classic logic puzzle. \(You do not need to know Fillomino in order to solve this problem.\) In one classroom in Yunqi town, some volunteers are playing a board game variant of it:

Consider an 𝑛n by 𝑛n chessboard. Its rows are numbered from 11 to 𝑛n from the top to the bottom. Its columns are numbered from 11 to 𝑛n from the left to the right. A cell on an intersection of 𝑥x-th row and 𝑦y-th column is denoted \(𝑥,𝑦\)\(x,y\). The main diagonal of the chessboard is cells \(𝑥,𝑥\)\(x,x\) for all 1≤𝑥≤𝑛1≤x≤n.

A permutation of {1,2,3,…,𝑛}{1,2,3,…,n} is written on the main diagonal of the chessboard. There is exactly one number written on each of the cells. The problem is to partition the cells under and on the main diagonal \(there are exactly 1+2+…+𝑛1+2+…+n such cells\) into 𝑛n connected regions satisfying the following constraints:

1. Every region should be connected. That means that we can move from any cell of a region to any other cell of the same region visiting only cells of the same region and moving from a cell to an adjacent cell.
2. The 𝑥x-th region should contain cell on the main diagonal with number 𝑥x for all 1≤𝑥≤𝑛1≤x≤n.
3. The number of cells that belong to the 𝑥x-th region should be equal to 𝑥x for all 1≤𝑥≤𝑛1≤x≤n.
4. Each cell under and on the main diagonal should belong to exactly one region.

Input

The first line contains a single integer 𝑛n \(1≤𝑛≤5001≤n≤500\) denoting the size of the chessboard.

The second line contains 𝑛n integers 𝑝1p1, 𝑝2p2, ..., 𝑝𝑛pn. 𝑝𝑖pi is the number written on cell \(𝑖,𝑖\)\(i,i\). It is guaranteed that each integer from {1,…,𝑛}{1,…,n} appears exactly once in 𝑝1p1, ..., 𝑝𝑛pn.Output

If no solution exists, output −1−1.

Otherwise, output 𝑛n lines. The 𝑖i-th line should contain 𝑖i numbers. The 𝑗j-th number on the 𝑖i-th line should be 𝑥x if cell \(𝑖,𝑗\)\(i,j\) belongs to the the region with 𝑥x cells.

```python
t = int(input())

data = [[0] * t for _ in range(t)]
nums = list(map(int, input().split()))
for i in range(t):
    data[i][i] = nums[i]
    
for i in range(t - 1, - 1 , -1 ):
    x = i 
    y = i 
    c = data[i][i]
    r = c - 1
    while r :
        if x + 1 < t and data[x + 1][y] == 0 :
            x += 1
        else:
            y -= 1
        data[x][y] = c 
        r -= 1
        
for i in range(len(data)):
    print(*data[i])
```



