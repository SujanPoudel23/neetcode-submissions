class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        cache = {}

        for i, n in enumerate(nums):
            cache[0 - n] = i

        for i in range(0, len(nums), 1):
            for j in range(i + 1, len(nums), 1):
                Sum = nums[i] + nums[j]

                if Sum in cache and i != cache[Sum] and j != cache[Sum]:
                    trip = nums[i], nums[j], -1 * (nums[i] + nums[j])
                    triplets.add(tuple(sorted(trip)))
        
        tempList = list(triplets)
        for i in range(len(tempList)):
            tempList[i] = list(tempList[i])

        return tempList

        