class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prod = 1

        for ind, n in enumerate(nums):
            if n == 0:
                prodZero = 1

                for i, j in enumerate(nums):
                    if i != ind:
                        prodZero *= j
                
                res[ind] = prodZero
                return res

            prod *= n
        
        return [int(prod / n) for n in nums]

                


