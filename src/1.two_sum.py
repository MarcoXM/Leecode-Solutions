class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            for j in range(l):
                if nums[i] + nums[j] == target:
                    return [i,j]
        # O(NN)

    def twoSum_(self, nums: List[int], target: int) -> List[int]):
        l = len(nums)
        dit = {}
        for i,v in enumerate(nums):
            if dit.get(target - v)!= None:
                return [i,dit.get(target - v)]
            dit[v] = i

        # O(N)