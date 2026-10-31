class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_list = sorted(nums)
        curr = 0
        maxc = 0

        for i, v in enumerate(sorted_list):
            if i + 1 >= len(sorted_list):
                break
            
            if v + 1 == sorted_list[i + 1]:
                curr += 1
            elif v == sorted_list[i + 1]:
                continue
            else:
                curr = 0
            
            maxc = max(curr, maxc)
    
        return maxc + 1
