class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=k=0
        string=[]
        word1=list(word1)
        word2=list(word2)

        while i<len(word1) or j<len(word2):  
            if i<len(word1):
                string.append(word1[i])
                i+=1

            if j<len(word2):
                string.append(word2[j])
                j+=1

        return "".join(string)
            

            


        