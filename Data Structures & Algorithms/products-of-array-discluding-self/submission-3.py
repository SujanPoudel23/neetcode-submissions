class Solution:
    '''
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
    '''

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_cprod = nums.copy()
        right_cprod = nums.copy()
        result = [0] * len(nums)

        for i in range(1, len(nums), 1):
            left_cprod[i] =  left_cprod[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            right_cprod[i] = right_cprod[i + 1] * nums[i]
        
        result[0] = right_cprod[1]
        result[len(result) -1] = left_cprod[len(result) - 2]
        for i in range(1, len(result) - 1):
            result[i] = left_cprod[i-1] * right_cprod[i+1]
    
        return result

            