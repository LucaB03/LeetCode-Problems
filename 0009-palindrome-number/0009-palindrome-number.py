class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        for i in range(0, int(len(x)/2)):
            if x[i] != x[len(x)-1-i]:
                return False
        return True