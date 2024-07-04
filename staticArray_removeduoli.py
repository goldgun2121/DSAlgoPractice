class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L+=1
        return L

solution = Solution()
print(solution.removeDuplicates([1,1,2]))