class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * (2*len(nums))
        for i in range(len(nums)):
            ans[i], ans[i+len(nums)] = nums[i], nums[i]
        return ans

solution = Solution()
print(solution.getConcatenation([1,2,1]))