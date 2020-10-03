# LCP 03. 机器人大冒险

> 力扣团队买了一个可编程机器人，机器人初始位置在原点\(0, 0\)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：
>
> U: 向y轴正方向移动一格 R: 向x轴正方向移动一格。 不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。
>
> 给定终点坐标\(x, y\)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。
>
> 示例 1：
>
> 输入：command = "URR", obstacles = \[\], x = 3, y = 2 输出：true 解释：U\(0, 1\) -&gt; R\(1, 1\) -&gt; R\(2, 1\) -&gt; U\(2, 2\) -&gt; R\(3, 2\)。 示例 2：
>
> 输入：command = "URR", obstacles = \[\[2, 2\]\], x = 3, y = 2 输出：false 解释：机器人在到达终点前会碰到\(2, 2\)的障碍物。 示例 3：
>
> 输入：command = "URR", obstacles = \[\[4, 2\]\], x = 3, y = 2 输出：true 解释：到达终点后，再碰到障碍物也不影响返回结果。
>
> 限制：
>
> 2 &lt;= command的长度 &lt;= 1000 command由U，R构成，且至少有一个U，至少有一个R 0 &lt;= x &lt;= 1e9, 0 &lt;= y &lt;= 1e9 0 &lt;= obstacles的长度 &lt;= 1000 obstacles\[i\]不为原点或者终点

{% tabs %}
{% tab title="Python" %}
```
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:

        ## 一开始以为很难的题目
        ## 结果真的是很难 
        paths = set()
        paths.add((0,0))
        i,j = 0, 0
        for c in command:
            if c == "U":
                j += 1
            else:
                i += 1
            paths.add((i,j))
        num_loop = min(x//i, y//j)
        # print(num_loop)
        # print( x - num_loop * i, y - num_loop * j )
        if ( x - num_loop * i, y - num_loop * j ) not in paths:
            return False
        print(paths)
        for obs in obstacles:
            num_loop = min(obs[0]//i,obs[1]//j)
            print(obs[0] - num_loop * i , obs[1] - num_loop* j)
            if obs[0] <= x and obs[1] <= y and (obs[0] - num_loop * i , obs[1] - num_loop* j) in paths:
                return False
        return True
```
{% endtab %}

{% tab title="Python-TLE" %}
```python
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:

        ## 一开始以为很难的题目
        start = [0, 0]
        idx = 0
        obs = set(map(tuple,obstacles))
        # print(obs)
        while start[0] <= x and start[1] <= y:
            move = command[idx%len(command)] 
            if move == "U" :
                start[1] += 1
            else:
                start[0] += 1
            idx += 1
            if start[0] ==x and start[1]== y:
                return True
            elif tuple(start) in obs:
                return False

        # print(idx,start)
        return False
```
{% endtab %}
{% endtabs %}

