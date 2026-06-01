class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        answer = 0

        i = 0
        while i < len(tokens):
            if tokens[i] == "+":
                tokens[i] = int(tokens[i-2]) + int(tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-2)
                i = 0
            if tokens[i] == "-":
                tokens[i] = int(tokens[i-2]) - int(tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-2)
                i = 0
            if tokens[i] == "*":
                tokens[i] = int(tokens[i-2]) * int(tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-2)
                i = 0
            if tokens[i] == "/":
                tokens[i] = int(tokens[i-2]) / int(tokens[i-1])
                tokens.pop(i-1)
                tokens.pop(i-2)
                i = 0
            print(tokens)
            answer = int(tokens[0])
            i += 1

        return answer