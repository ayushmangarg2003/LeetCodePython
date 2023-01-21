class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.ParkingSystem = [big , medium , small]

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.ParkingSystem[0] > 0:
            self.ParkingSystem[0] -=1
            return 1
        if carType ==2 and self.ParkingSystem[1] >0:
            self.ParkingSystem[1] -=1
            return 1
        if carType ==3 and self.ParkingSystem[2] >0:
            self.ParkingSystem[2] -=1
            return 1
        return 0
