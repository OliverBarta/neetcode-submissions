class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if len(temperatures) == 0:
            return []

        output = []

        for i in range(len(temperatures)-1):
            higherTempFound = False
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    output.append(j-i)
                    higherTempFound = True
                    break
            if not higherTempFound:
                output.append(0)

        output.append(0)

        return output