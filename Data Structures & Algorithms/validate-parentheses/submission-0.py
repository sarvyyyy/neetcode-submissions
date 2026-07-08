class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        def peek(x):
            if len(x)==0:
                return None
            return x[-1]
        for i in range(len(s)):
            if s[i]==')' and peek(stack)=="(" or s[i]=="}" and peek(stack)=="{" or s[i]=="]" and peek(stack)=="[":
                stack.pop()
            elif s[i] in ['(','[',"{"]:
                stack.append(s[i])
            else:
                return False
        if stack == []:
            return True
        else:
            return False