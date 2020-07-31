# 面试题 08.03. 魔术索引

```cpp
class Solution {
public:
    int findMagicIndex(vector<int>& nums) {
        if(nums.size() == 0)return -1;
        int left = 0 , right = nums.size();
        return find(nums,left,right);
    }
    int find(vector<int>& nums, int left,int right){
        if(left == right)return -1;
        int mid = left + (right - left) / 2;
        int left_val = find(nums,left,mid);
        if(left_val != -1)return left_val;
        else if(nums[mid] == mid)return mid;
        return find(nums ,mid + 1, right);
    }
};
```

