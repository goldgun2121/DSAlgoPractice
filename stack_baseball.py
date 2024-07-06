class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record = []
        count, sum = 0, 0
        for i in operations:
            if i == "+" and count > 1:
                record.append(int(record[-1] + record[-2]))
                sum = sum + record[-1]
                count += 1
            elif i == "D" and count > 0:
                record.append(int(2 * record[-1]))
                sum = sum + record[-1]
                count += 1
            elif i == "C" and count > 0:
                sum = sum - record[-1]
                record.pop()
                count -= 1
            else:
                record.append(int(i))
                sum = sum + record[-1]
                count += 1
        return sum

solution = Solution()
print(solution.calPoints(["5","2","C","D","+"]))