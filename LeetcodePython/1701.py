class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        act = customers[0][0]
        wait = 0
        for i in customers:
            if act<i[0]:
                act = i[0]
            act += i[1]
            wait +=(act - i[0])
        return wait/len(customers)
