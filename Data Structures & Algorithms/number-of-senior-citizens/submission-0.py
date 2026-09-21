class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for st in details:
            st=st[::-1]
            st2=st[2:4]
            st2=st2[::-1]
            if int(st2)>60:
                count+=1
        
        return count