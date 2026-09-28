class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maximum=0

        for char in s:
            if char=='(':
                count+=1
                maximum=max(count,maximum)

            if char==')':
                count-=1

        return maximum

        