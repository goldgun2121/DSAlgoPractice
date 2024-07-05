class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        L = 0
        for R in range(len(nums)):
            print("R", R)
            if nums[R] != val:
                nums[L] = nums[R]
                L += 1
        print(nums)
        return L

solution = Solution()
print(solution.removeElement([0,1,2,2,3,0,4,2], 2))