class Solution:
    def isValid(self, s: str) -> bool:
        
        numC = []
        
        for i in s:
            if i == "(":
                numC.append(1)
            elif i == "[":
                numC.append(2)
            elif i == "{":
                numC.append(3)
            elif i == ")":
                numC.append(4)
            elif i == "]":
                numC.append(5)
            elif i == "}":
                numC.append(6)
        i = 0

        while i < len(numC)-1:

            if numC[i]+3 == numC[i+1]:
                numC.pop(i)
                numC.pop(i)
                i = 0
            else:
                i += 1

        print(numC)
        if numC == []:
            return True

        return False