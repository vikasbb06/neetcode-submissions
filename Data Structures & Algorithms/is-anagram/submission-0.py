class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sseen={}
        tseen={}

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            sseen[s[i]]=sseen.get(s[i],0)+1
            tseen[t[i]]=tseen.get(t[i],0)+1

        return sseen==tseen