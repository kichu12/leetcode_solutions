class Solution:
    def isPalindrome(self, x: int) -> bool:
        h=False
        g=str(x)
        j=g[::-1]
        if j == g:
            h=True
        else:
            h=False
        return h