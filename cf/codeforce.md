# Codeforces Round \#717 \(Div. 2\)



A. Tit for Tattime limit per test1 secondmemory limit per test256 megabytesinputstandard inputoutputstandard output

Given an array 𝑎a of length 𝑛n, you can do at most 𝑘k operations of the following type on it:

* choose 22 different elements in the array, add 11 to the first, and subtract 11 from the second. However, all the elements of 𝑎a have to remain non-negative after this operation.

What is lexicographically the smallest array you can obtain?

An array 𝑥x is [lexicographically smaller](https://en.wikipedia.org/wiki/Lexicographical_order) than an array 𝑦y if there exists an index 𝑖i such that 𝑥𝑖&lt;𝑦𝑖xi&lt;yi, and 𝑥𝑗=𝑦𝑗xj=yj for all 1≤𝑗&lt;𝑖1≤j&lt;i. Less formally, at the first index 𝑖i in which they differ, 𝑥𝑖&lt;𝑦𝑖xi&lt;yi.Input

The first line contains an integer 𝑡t \(1≤𝑡≤201≤t≤20\) – the number of test cases you need to solve.

The first line of each test case contains 22 integers 𝑛n and 𝑘k \(2≤𝑛≤1002≤n≤100, 1≤𝑘≤100001≤k≤10000\) — the number of elements in the array and the maximum number of operations you can make.

The second line contains 𝑛n space-separated integers 𝑎1a1, 𝑎2a2, ……, 𝑎𝑛an \(0≤𝑎𝑖≤1000≤ai≤100\) — the elements of the array 𝑎a.Output

For each test case, print the lexicographically smallest array you can obtain after at most 𝑘k operations.

```python
t = int(input())
## 贪心！ 
for _ in range(t):
    n, k  = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    # print(nums)
    i = 0
    while k and i < n:
        if nums[i] >  0:
            diff = min(k , nums[i])
            nums[i] -= diff
            k = k - diff
            nums[-1] += diff
        i += 1
    print(*nums)
```



B. AGAGA XOOORRRtime limit per test1 secondmemory limit per test256 megabytesinputstandard inputoutputstandard output

Baby Ehab is known for his love for a certain operation. He has an array 𝑎a of length 𝑛n, and he decided to keep doing the following operation on it:

* he picks 22 adjacent elements; he then removes them and places a single integer in their place: their [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR). Note that the length of the array decreases by one.

Now he asks you if he can make all elements of the array equal. Since babies like to make your life harder, he requires that you leave at least 22 elements remaining.Input

The first line contains an integer 𝑡t \(1≤𝑡≤151≤t≤15\) — the number of test cases you need to solve.

The first line of each test case contains an integers 𝑛n \(2≤𝑛≤20002≤n≤2000\) — the number of elements in the array 𝑎a.

The second line contains 𝑛n space-separated integers 𝑎1a1, 𝑎2a2, ……, 𝑎𝑛an \(0≤𝑎𝑖&lt;2300≤ai&lt;230\) — the elements of the array 𝑎a.Output

If Baby Ehab can make all elements equal while leaving at least 22 elements standing, print "YES". Otherwise, print "NO".

{% tabs %}
{% tab title="Python- TLE" %}
```python
n = int(input())
 
nums = list(map(int,input().split()))
# print(nums)
 
from itertools import chain, combinations
x = 20000
res = []  
def dfs(nums, pth):
    global x
    global res
    if len(nums) >= 2 and check(nums):
        # print(pth,nums)
        if len(pth) < x:
            res = pth[:]
            x = len(pth)
        return 
    for i in range(len(nums)):
        pth.append(nums[i])
        dfs(nums[:i] + nums[i + 1:], pth)
        pth.pop()
    
 
def check(nums):
    s = sum(nums)
    if s & 1 :return True
    a = list(map(sum,chain.from_iterable(combinations(nums, r) for r in range(len(nums) - 1,0,-1))))
    # print(s, a)
    
    return s//2 not in set(a)
    
dfs(nums,[])
print(x if x != 20000 else 0 )
print(*res ) if res else None

```
{% endtab %}

{% tab title="C ++" %}
```cpp
#include <bits/stdc++.h>
using namespace std;
int pre[2005];
int main()
{
    int t;
    scanf("%d",&t);
    while (t--)
    {
        int n;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
        {
            int a;
            scanf("%d",&a);
            pre[i]=(pre[i-1]^a);
        }
        bool yes=!pre[n];
        for (int i=1;i<=n;i++)
        {
            for (int j=i+1;j<n;j++)
            yes|=(pre[i]==(pre[j]^pre[i]) && pre[i]==(pre[n]^pre[j]));
        }
        puts(yes? "YES":"NO");
    }
}
```
{% endtab %}
{% endtabs %}

C. Baby Ehab Partitions Againtime limit per test2 secondsmemory limit per test256 megabytesinputstandard inputoutputstandard output

Baby Ehab was toying around with arrays. He has an array 𝑎a of length 𝑛n. He defines an array to be good if there's no way to partition it into 22 subsequences such that the sum of the elements in the first is equal to the sum of the elements in the second. Now he wants to remove the minimum number of elements in 𝑎a so that it becomes a good array. Can you help him?

A sequence 𝑏b is a subsequence of an array 𝑎a if 𝑏b can be obtained from 𝑎a by deleting some \(possibly zero or all\) elements. A partitioning of an array is a way to divide it into 22 subsequences such that every element belongs to exactly one subsequence, so you must use all the elements, and you can't share any elements.Input

The first line contains an integer 𝑛n \(2≤𝑛≤1002≤n≤100\) — the length of the array 𝑎a.

The second line contains 𝑛n integers 𝑎1a1, 𝑎2a2, ……, 𝑎𝑛an \(1≤𝑎𝑖≤20001≤ai≤2000\) — the elements of the array 𝑎a.Output

The first line should contain the minimum number of elements you need to remove.

The second line should contain the indices of the elements you're removing, separated by spaces.

We can show that an answer always exists. If there are multiple solutions, you can print any.

{% tabs %}
{% tab title="Python - TLE" %}
```python
n = int(input())
 
nums = list(map(int,input().split()))
# print(nums)
 
from itertools import chain, combinations
x = 20000
res = []  
def dfs(nums, pth):
    global x
    global res
    if len(nums) >= 2 and check(nums):
        # print(pth,nums)
        if len(pth) < x:
            res = pth[:]
            x = len(pth)
        return 
    for i in range(len(nums)):
        pth.append(nums[i])
        dfs(nums[:i] + nums[i + 1:], pth)
        pth.pop()
    
 
def check(nums):
    s = sum(nums)
    if s & 1 :return True
    a = list(map(sum,chain.from_iterable(combinations(nums, r) for r in range(len(nums) - 1,0,-1))))
    # print(s, a)
    
    return s//2 not in set(a)
    
dfs(nums,[])
print(x if x != 20000 else 0 )
print(*res ) if res else None
```
{% endtab %}

{% tab title="c++" %}
```cpp
#include <bits/stdc++.h>
using namespace std;
int n;
bool bad(vector<int> v)
{
    int s=0;
    for (int i:v)
    s+=i;
    if (s%2)
    return 0;
    bitset<200005> b;
    b[0]=1;
    for (int i:v)
    b|=(b<<i);
    return b[s/2];
}
int main()
{
    scanf("%d",&n);
    vector<int> v(n);
    for (int i=0;i<n;i++)
    scanf("%d",&v[i]);
    if (bad(v))
    {
        pair<int,int> mn(20,0);
        for (int i=0;i<n;i++)
        mn=min(mn,make_pair(__builtin_ctz(v[i]),i+1));
        printf("1\n%d",mn.second);
    }
    else
    printf("0");
}
```
{% endtab %}
{% endtabs %}

