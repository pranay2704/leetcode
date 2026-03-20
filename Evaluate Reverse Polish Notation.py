class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        for i in tokens:
            if i == '*':
                result = num.pop() * num.pop()
                num.append(result)
            elif i == '-':
                n1 = num.pop()
                n2 = num.pop()
                result = n2 - n1
                num.append(result)
            elif i == '/':
                n1 = num.pop()
                n2 = num.pop()
                result = n2 // n1
                if result<0:
                    result=(abs(n2)//abs(n1))*(-1)
                num.append(result)
            elif i == '+':
                result = num.pop() + num.pop()
                num.append(result)
            else:
                num.append(int(i))
            print(i, num[-1])
        print(num)
        return num[0]
