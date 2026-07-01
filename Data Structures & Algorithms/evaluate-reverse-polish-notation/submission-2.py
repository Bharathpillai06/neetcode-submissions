class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            x = []    
            for y in tokens:
                if y not in ["+", "-", "*", "/"]:
                   x.append(int(y))
                else:
                    z = x.pop()
                    if y == "+":
                        ans = x.pop() + z
                    if y == "-":
                        ans = x.pop() - z
                    if y == "*":
                        ans = x.pop() * z
                    if y == "/":
                        ans = int(x.pop() / z)
                    x.append(ans)

            return x[0]
                


        
        