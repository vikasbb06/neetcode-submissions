class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n #an array is creted of 1's
        
        left_sideproduct=1
        for i in range(n): # left side product
            res[i]=left_sideproduct
            left_sideproduct*=nums[i]

        right_sideproduct=1
        #caluclate the right side product with the left side
        for i in range(n-1,-1,-1):
            res[i] *=right_sideproduct
            right_sideproduct*=nums[i]

        return res

        