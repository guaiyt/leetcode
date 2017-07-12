class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        s = '0'
        if (x > 2147483647) | (x < -2147483647):
            s = '0'
            flag = 0
        elif (x > 0):# & (x <= 1073741824):
            s = str(x)
            flag = -1
        elif (x < 0):# & (x >= -1073741824):
            s = str(-x)
            flag = 1
        s = s[::-1]
        if (int(s) > 2147483647) | (int(s) < -2147483647):
            flag = 0
        return -1 * flag * int(s)
            