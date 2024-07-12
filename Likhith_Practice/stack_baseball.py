class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        sum = 0
        for i in operations:
            if i == "+" and len(record) > 1:
                record.append(int(record[-1] + record[-2]))
                sum = sum + record[-1]
            elif i == "D" and len(record) > 0:
                record.append(int(2 * record[-1]))
                sum = sum + record[-1]
            elif i == "C" and len(record) > 0:
                sum = sum - record[-1]
                record.pop()
            else:
                record.append(int(i))
                sum = sum + record[-1]
        return sum

solution = Solution()
print(solution.calPoints(["C","5","2","C","D","+"]))