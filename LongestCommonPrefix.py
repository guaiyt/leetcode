class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            buf = ""
            for i in list(strs[0]):
                buf += i
                for j in list(strs[1:]):
                    if buf != j[:len(buf)]:
                        return buf[:-1]
            return buf
            