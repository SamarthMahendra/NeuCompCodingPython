class ParkingLot:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.available = capacity

    def park_car(self):
        if self.available > 0:
            self.available -= 1
            return True
        else:
            return False

    def is_full(self):
        return not (self.available)


from abc import ABC, abstractmethod

class ParkingSystemInterface(ABC):

        @abstractmethod
        def addCar(self, carType: int) -> bool:
            pass




class ParkingSystem(ParkingSystemInterface):

    def __init__(self, big: int, medium: int, small: int):
        self.lots = {
            1: ParkingLot(big),
            2: ParkingLot(medium),
            3: ParkingLot(small)
        }

    def addCar(self, carType: int) -> bool:
        return self.lots[carType].park_car()

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)