class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newChar = {')': '(',
                   '}': '{',
                   ']': '['}
        
        newList = []
        
        if len(s) < 2:
            return False
        
        L=0
        
        for R in range(len(s)):
            if s[R] in newChar.values():
                newList.append(s[R])
            else:
                if newChar[s[R]] not in newList:
                    return False
        return True
                
solution = Solution()
print(solution.isValid("{[]}"))