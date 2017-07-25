class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        i, k, a = 0, len(nums), 0
        a = 0 if a != nums[0] else 1
        while i < k:
            if nums[i] != a:
                a = nums[i]
                i += 1
            else:
                nums.pop(i)
                k -= 1
        return len(nums)