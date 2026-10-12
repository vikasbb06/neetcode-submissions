class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.replace(" ","").lower()
        s1=re.sub(r'[^a-zA-Z0-9]', '',s1)
        s2=s1[::-1]

        return s2==s1


        