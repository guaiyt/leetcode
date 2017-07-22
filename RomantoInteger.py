class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        buf = []
        sum = 0
        transform = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I': 1}
        # D 500 C 100 X 10 V 5 I 1
        for i in range(0, len(l) - 1):
            if transform[l[i]] < transform[l[i+1]]:
                sum -= transform[l[i]]
            else:
                sum += transform[l[i]]
        return sum + transform[l[-1]]
            
            