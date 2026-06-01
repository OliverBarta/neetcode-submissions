class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        hours = [0] * len(speed)


        for i in range(len(speed)):
            hours[i] = (target - position[i]) / speed[i]
        
        # sort into descending order

        i = 0
        while i < len(hours)-1:
            
            j = i + 1
            while j < len(hours):
                if hours[i] >= hours[j]:
                    j += 1
                else:
                    tempH = hours[j]
                    tempP = position[j]
                    tempS = speed[j]
                    
                    hours[j] = hours[i]
                    hours[i] = tempH

                    position[j] = position[i]
                    position[i] = tempP

                    speed[j] = speed[i]
                    speed[i] = tempS
                    j = i + 1
            i += 1

        #
        
        # print(position)
        # print(speed)
        # print(hours)

        i = 0
        while i < len(speed)-1:
            j = i + 1
            while j < len(speed):
                if position[i] > position[j]:
                    position.pop(j)
                    speed.pop(j)
                    hours.pop(j)
                else:
                    j += 1
            i += 1
        
        print(position)
        print(speed)
        print(hours)

        seen = []
        output = 0

        # counts how many unique values are in hours
        for i in range(len(hours)):
            if hours[i] not in seen:
                output += 1
                seen.append(hours[i])

        return output

