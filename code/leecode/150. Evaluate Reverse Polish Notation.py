class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ch = ["+", "-", "*", "/"]
        s = []
        for i in tokens:
            if i not in ch:
                s.append(i)
            else:
                a = s.pop()
                b = s.pop()
                c = eval(b+i+a)
                c=int(c)
                s.append(str(c))
        ans = int(s[0])
        return ans


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11",
      "*", "/", "*", "17", "+", "5", "+"]))

import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # 定义操作符对应的函数
        op_to_binary_fn = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y),  
        }

        stack = []
        for token in tokens:
            if token not in op_to_binary_fn:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                result = op_to_binary_fn[token](b, a)
                stack.append(result)
        
        return stack[0]