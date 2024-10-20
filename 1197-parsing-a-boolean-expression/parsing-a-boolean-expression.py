class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops = {'!','|','&'}
        stack = []
        for n in expression:
            if n in ops:
                stack.append(n)
            elif n in {'t','f'}:
                stack.append(n == 't')
            elif n == ')':
                OR, AND = False, True
                while stack[-1] not in ops:
                    lastBool = stack.pop()
                    OR |= lastBool
                    AND &= lastBool
                lastOp = stack.pop()
                if lastOp == '!':
                    stack.append(not OR)
                elif lastOp == '&':
                    stack.append(AND)
                elif lastOp == '|':
                    stack.append(OR)
        return stack.pop()
