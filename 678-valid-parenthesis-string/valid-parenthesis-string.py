class Solution:
    def checkValidString(self, s: str) -> bool:
        
        open_brackets = []
        asterisks = []

        for i, c in enumerate(s):

            if c == '(':
                open_brackets.append(i)

            elif c == '*':
                asterisks.append(i)

            else:
                if open_brackets:
                    open_brackets.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
                
        while open_brackets and asterisks:

            if open_brackets.pop() > asterisks.pop():
                return False
            
        return not open_brackets
