class Solution(object):
    def isValid(self, s):
        stack =[]
        dict = { ")" : "(" , "}" : "{" , "]" : "[" }
        for i in s:
            if i in dict.keys():
                if stack and stack[-1]==dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
