class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr2=arr[::-1]
        prev_max = arr2[0]
        arr2[0] = -1
        for i in range(1,len(arr2)):
            curr = arr2[i] 
            arr2[i]=prev_max
            if curr > prev_max: 
                prev_max = curr
        arr2=arr2[::-1]
        return arr2
        
        