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

### 通用模板

```python
def binarySearch(nums, target):
    l, r = 0, len(nums)
    while l < n:
        mid = l + (n - l ) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid ### r 是闭区间
    return l 
```

### 变题

1. **查找第一个不小于目标值的数，可变形为查找最后一个小于目标值的数**

```python
## 
```

1. \*\*\*\*
2. \*\*\*\*

