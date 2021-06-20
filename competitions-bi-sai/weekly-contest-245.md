# weekly-contest-245



不错

1903. Largest Odd Number in String

> You are given a string `num`, representing a large integer. Return _the **largest-valued odd** integer \(as a string\) that is a **non-empty substring** of_ `num`_, or an empty string_ `""` _if no odd integer exists_.
>
> A **substring** is a contiguous sequence of characters within a string.
>
> **Example 1:**
>
> ```text
> Input: num = "52"
> Output: "5"
> Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
> ```
>
> **Example 2:**
>
> ```text
> Input: num = "4206"
> Output: ""
> Explanation: There are no odd numbers in "4206".
> ```
>
> **Example 3:**
>
> ```text
> Input: num = "35427"
> Output: "35427"
> Explanation: "35427" is already an odd number.
> ```
>
> **Constraints:**
>
> * `1 <= num.length <= 105`
> * `num` only consists of digits and does not contain any leading zeros.

```python
class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx = len(num)
        for i in range(len(num) - 1,- 1, - 1):
            if int(num[i]) % 2 :
                idx = i
                break
                
        if idx != len(num):
            return num[:idx + 1]
        return ""
        
        
```



1904. The Number of Full Rounds You Have Played

> A new online video game has been released, and in this video game, there are **15-minute** rounds scheduled every **quarter-hour** period. This means that at `HH:00`, `HH:15`, `HH:30` and `HH:45`, a new round starts, where `HH` represents an integer number from `00` to `23`. A **24-hour clock** is used, so the earliest time in the day is `00:00` and the latest is `23:59`.
>
> Given two strings `startTime` and `finishTime` in the format `"HH:MM"` representing the exact time you **started** and **finished** playing the game, respectively, calculate the **number of full rounds** that you played during your game session.
>
> * For example, if `startTime = "05:20"` and `finishTime = "05:59"` this means you played only one full round from `05:30` to `05:45`. You did not play the full round from `05:15` to `05:30` because you started after the round began, and you did not play the full round from `05:45` to `06:00` because you stopped before the round ended.
>
> If `finishTime` is **earlier** than `startTime`, this means you have played overnight \(from `startTime` to the midnight and from midnight to `finishTime`\).
>
> Return _the **number of full rounds** that you have played if you had started playing at_ `startTime` _and finished at_ `finishTime`.
>
> **Example 1:**
>
> ```text
> Input: startTime = "12:01", finishTime = "12:44"
> Output: 1
> Explanation: You played one full round from 12:15 to 12:30.
> You did not play the full round from 12:00 to 12:15 because you started playing at 12:01 after it began.
> You did not play the full round from 12:30 to 12:45 because you stopped playing at 12:44 before it ended.
> ```
>
> **Example 2:**
>
> ```text
> Input: startTime = "20:00", finishTime = "06:00"
> Output: 40
> Explanation: You played 16 full rounds from 20:00 to 00:00 and 24 full rounds from 00:00 to 06:00.
> 16 + 24 = 40.
> ```
>
> **Example 3:**
>
> ```text
> Input: startTime = "00:00", finishTime = "23:59"
> Output: 95
> Explanation: You played 4 full rounds each hour except for the last hour where you played 3 full rounds.
> ```
>
> **Constraints:**
>
> * `startTime` and `finishTime` are in the format `HH:MM`.
> * `00 <= HH <= 23`
> * `00 <= MM <= 59`
> * `startTime` and `finishTime` are not equal.



1905. Count Sub Islands

> You are given two `m x n` binary matrices `grid1` and `grid2` containing only `0`'s \(representing water\) and `1`'s \(representing land\). An **island** is a group of `1`'s connected **4-directionally** \(horizontal or vertical\). Any cells outside of the grid are considered water cells.
>
> An island in `grid2` is considered a **sub-island** if there is an island in `grid1` that contains **all** the cells that make up **this** island in `grid2`.
>
> Return the _**number** of islands in_ `grid2` _that are considered **sub-islands**_.
>
> **Example 1:**![](https://assets.leetcode.com/uploads/2021/06/10/test1.png)
>
> ```text
> Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
> Output: 3
> Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
> The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
> ```
>
> **Example 2:**![](https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png)
>
> ```text
> Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
> Output: 2 
> Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
> The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
> ```
>
> **Constraints:**
>
> * `m == grid1.length == grid2.length`
> * `n == grid1[i].length == grid2[i].length`
> * `1 <= m, n <= 500`
> * `grid1[i][j]` and `grid2[i][j]` are either `0` or `1`.



1906. Minimum Absolute Difference Queries

> The **minimum absolute difference** of an array `a` is defined as the **minimum value** of `|a[i] - a[j]|`, where `0 <= i < j < a.length` and `a[i] != a[j]`. If all elements of `a` are the **same**, the minimum absolute difference is `-1`.
>
> * For example, the minimum absolute difference of the array `[5,2,3,7,2]` is `|2 - 3| = 1`. Note that it is not `0` because `a[i]` and `a[j]` must be different.
>
> You are given an integer array `nums` and the array `queries` where `queries[i] = [li, ri]`. For each query `i`, compute the **minimum absolute difference** of the **subarray** `nums[li...ri]` containing the elements of `nums` between the **0-based** indices `li` and `ri` \(**inclusive**\).
>
> Return _an **array**_ `ans` _where_ `ans[i]` _is the answer to the_ `ith` _query_.
>
> A **subarray** is a contiguous sequence of elements in an array.
>
> The value of `|x|` is defined as:
>
> * `x` if `x >= 0`.
> * `-x` if `x < 0`.
>
> **Example 1:**
>
> ```text
> Input: nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
> Output: [2,1,4,1]
> Explanation: The queries are processed as follows:
> - queries[0] = [0,1]: The subarray is [1,3] and the minimum absolute difference is |1-3| = 2.
> - queries[1] = [1,2]: The subarray is [3,4] and the minimum absolute difference is |3-4| = 1.
> - queries[2] = [2,3]: The subarray is [4,8] and the minimum absolute difference is |4-8| = 4.
> - queries[3] = [0,3]: The subarray is [1,3,4,8] and the minimum absolute difference is |3-4| = 1.
> ```
>
> **Example 2:**
>
> ```text
> Input: nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
> Output: [-1,1,1,3]
> Explanation: The queries are processed as follows:
> - queries[0] = [2,3]: The subarray is [2,2] and the minimum absolute difference is -1 because all the
>   elements are the same.
> - queries[1] = [0,2]: The subarray is [4,5,2] and the minimum absolute difference is |4-5| = 1.
> - queries[2] = [0,5]: The subarray is [4,5,2,2,7,10] and the minimum absolute difference is |4-5| = 1.
> - queries[3] = [3,5]: The subarray is [2,7,10] and the minimum absolute difference is |7-10| = 3.
> ```
>
> **Constraints:**
>
> * `2 <= nums.length <= 105`
> * `1 <= nums[i] <= 100`
> * `1 <= queries.length <= 2 * 104`
> * `0 <= li < ri < nums.length`









