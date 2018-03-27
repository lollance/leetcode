class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if len(str(x)) < 1:
            return True
        
        for i in range(len(str(x))//2):
            if not str(x)[i] == str(x)[len(str(x))-i-1]:
                return False
        return True
