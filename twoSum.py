class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a, b = {}, {}
        j = 0
        for i in range(len(nums)):
            if nums[i] > target / 2:
                b[nums[i]] = i
            elif nums[i] < target / 2:
                a[nums[i]] = i
            elif nums[i] == target / 2:
                if j % 2 == 0:
                    a[nums[i]] = i
                else:
                    b[nums[i]] = i
                j += 1
        for k in a.keys():
            if target - k in b.keys():
                return [a.get(k), b.get(target - k)]