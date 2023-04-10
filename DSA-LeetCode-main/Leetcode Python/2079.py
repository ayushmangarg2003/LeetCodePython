class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1
        curcapacity = capacity
        for i in range(len(plants) - 1):
            curcapacity -= plants[i] 
            if curcapacity < plants[i + 1]: 
                steps += (i + 1) * 2 + 1 
                curcapacity = capacity  
            else:
                steps += 1
        return steps
