class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        try:
            for i in range(nums.count(val)):
                nums.remove(val)
        except:
            pass
        return len(nums)