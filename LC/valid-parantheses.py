class Solution():
    def isValid(self, s):
        matches_dict = {')':'(',']':'[','}' : '{' }
        stk = []
        for char in s:
            if char in matches_dict:
                if len(stk) == 0:
                    return False
                top = stk.pop()
                if top != matches_dict[char]:
                    return False
                
            else:
                stk.append(char)
                
        return not stk
            
            

solution = Solution()
print(solution.isValid("()"))      # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))      # False
print(solution.isValid("([)]"))    # False

            