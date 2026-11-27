class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        for i in range(1,len(nums)):
            anchor=nums[i]
            j=i-1
            while j>=0 and anchor<nums[j]:
                nums[j+1],nums[j]=nums[j],nums[j+1]
                j=j-1
            nums[j+1]=anchor



        