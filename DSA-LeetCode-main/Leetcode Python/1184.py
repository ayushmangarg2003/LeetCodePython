class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            return min(sum(distance[start:destination]), 
            sum(distance[:start])+sum(distance[destination:]))
        elif destination < start :
            return min(sum(distance[destination:start]), 
            sum(distance[:destination])+sum(distance[start:]))
