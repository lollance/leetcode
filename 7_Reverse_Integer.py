class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        ne = 0
        if x < 0:
            ne = 1
            x *= -1
            
        while x > 0:
            result *= 10
            result += x%10
            x //= 10
        if result > 2147483647:
            return 0            
        if ne == 0:
            return result
        else :
            return result*-1
