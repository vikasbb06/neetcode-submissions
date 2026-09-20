class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list2=nums
        nums.extend(list2)
        return nums