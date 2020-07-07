# Binary-Search

1. **从概率论的角度为什么我们要二分,因为可以更好的均摊风险..**
2. **好处:lgN复杂度,坏处是data need preprocessing into sorted. 所以加之其作用对象是array, 所以其实适用场景是多次查询,如果涉及插入和删除它不适用.**
3. **大型数据无足够的内存也不适合二分查询**

## 二分基本特征

1. 二分查询函数返回的是区间, 要查找的函数所在的可能的区间.
2. 中点mid 的选择 :

   > mid = left + \(right - left\)//2  \#\# 这个没什么好说的统一此格式
   >
   > 中点应该在闭区间方向向中心靠近

3. 理解 loop invariant:

   1. 搜索范围`[first, last)`不为空，即`first < last`  
   2. 搜索范围`[first, last)`左侧，即`[first0, first)`内所有元素\(若存在\)，都小于`value`其中`first0`是`first`的初始值
   3. 搜索范围`[first, last)`右侧，即`[last, last0)`内所有元素\(若存在\)，都大于等于`value`，其中`last0`是`last`的初始值.

   、

不断体会二分查找法的「减治思想」。

区间才是最重要的点！

### 通用模板

{% tabs %}
{% tab title="JAVA" %}
```java
public int search(int[] nums, int left, int right, int target) {
    while (left < right) {
        // 选择中位数时下取整
        int mid = left + (right - left) / 2;
        if (check(mid)) {
            // 下一轮搜索区间是 [mid + 1, right]
            left = mid + 1
        } else {
            // 下一轮搜索区间是 [left, mid]
            right = mid
        }
    }
    // 退出循环的时候，程序只剩下一个元素没有看到。
    // 视情况，是否需要单独判断 left（或者 right）这个下标的元素是否符合题意
}
```
{% endtab %}

{% tab title="CPP" %}
```cpp
int search(vector<int> &nums, int left, int right, int target) {
    while (left < right) {
        // 选择中位数时下取整
        int mid = left + (right - left) / 2;
        if (check(mid)) {
            // 下一轮搜索区间是 [mid + 1, right]
            left = mid + 1;
        } else {
            // 下一轮搜索区间是 [left, mid]
            right = mid;
        }
    }
    // 退出循环的时候，程序只剩下一个元素没有看到。
    // 视情况，是否需要单独判断 left（或者 right）这个下标的元素是否符合题意
}
```
{% endtab %}

{% tab title="Python" %}
```python
def search(nums: List[int], left: int, right: int, target: int) -> int:
    while left < right:
        # 选择中位数时下取整
        mid = left + (right - left) // 2
        if check(mid):
            # 下一轮搜索区间是 [mid + 1, right]
            left = mid + 1
        else:
            # 下一轮搜索区间是 [left, mid]
            right = mid
    # 退出循环的时候，程序只剩下一个元素没有看到。
    # 视情况，是否需要单独判断 left（或者 right）这个下标的元素是否符合题意
```
{% endtab %}

{% tab title="JavaScript" %}
```javascript
function search (nums, left, right, target) {
    while (left < right) {
        // 选择中位数时下取整
        let mid = left + ((right - left) >> 1)
        if (check(mid)) {
            // 下一轮搜索区间是 [mid + 1, right]
            left = mid + 1
        } else {
            // 下一轮搜索区间是 [left, mid]
            right = mid
        }
    }
    // 退出循环的时候，程序只剩下一个元素没有看到。
    // 视情况，是否需要单独判断 left（或者 right）这个下标的元素是否符合题意
}
```
{% endtab %}
{% endtabs %}

### 

理解模板代码的要点：

* 核心思想：核心思想只有一个，那就是：把待搜索的目标元素放在最后判断，每一次循环排除掉不存在目标元素的区间，目的依然是确定下一轮搜索的区间；
* 特征：`while (left < right)`，这里使用严格小于 `<` 表示的临界条件是：当区间里的元素只有 2 个时，依然可以执行循环体。换句话说，退出循环的时候一定有 `left == right` 成立，**这一点在定位元素下标的时候极其有用**；
* 在循环体中，先考虑 `nums[mid]` 在满足什么条件下不是目标元素，进而考虑两个区间 `[left, mid - 1]` 以及 `[mid + 1, right]` 里元素的性质，目的依然是确定下一轮搜索的区间；
* _**注意 1\***_**：**先考虑什么时候不是解，是一个经验，在绝大多数情况下不易出错，重点还是确定下一轮搜索的区间，由于这一步不容易出错，它的反面（也就是 `else` 语句的部分），就不用去考虑对应的区间是什么，直接从上一个分支的反面区间得到，进而确定边界如何设置；
* 根据边界情况，看取中间数的时候是否需要上取整；
* _**注意 2\***_**：** 这一步也依然是根据经验，建议先不要记住结论，在使用这个思想解决问题的过程中，去思考可能产生死循环的原因，进而理解什么时候需要在括号里加 1 ，什么时候不需要；
* 在退出循环以后，根据情况看是否需要对下标为 `left` 或者 `right` 的元素进行单独判断，这一步叫**「后处理」。**在有些问题中，排除掉所有不符合要求的元素以后，剩下的那 1 个元素就一定是目标元素。如果根据问题的场景，目标元素一定在搜索区间里，那么退出循环以后，可以直接返回 `left`（或者 `right`）

