class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, n in enumerate(nums):
            if n not in cache:
                cache[target - n] = i
            else:
                return [cache[n], i]
        


        