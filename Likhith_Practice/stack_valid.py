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
        
        for R in range(len(s)):
            if s[R] in newChar.values():
                newList.append(s[R])
            else:
                if len(newList) < 1:
                    return False
                else:
                    if newChar[s[R]] != newList.pop():
                        return False
        if len(newList) != 0:
            return False
        return True
 
 
#  code observed
    def isValidObserved(self, s):
        
        newChar = {')': '(',
                   '}': '{',
                   ']': '['}
        
        stack = []
        
        for c in s:
            if c in newChar:
                if stack and stack[-1] == newChar[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                
solution = Solution()
print(solution.isValid("){"))