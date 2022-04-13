'''
    Uber Pool Problem (medium)
    https://binarysearch.com/problems/Uber-Pool
'''

class Trip:
    def __init__(self, start_x=0, end_x=0, num_passengers=0):
        if start_x > end_x:
            raise ValueError('Destination cannot be before the Pickup')
        self.start_x = start_x
        self.end_x = end_x
        self.num_passengers = num_passengers

# trips can be of type Trips or
# array of [start_x: int, end_x: int, num_passengers: int]

class UberDriverInfo:
    def __init__(self, gas=0, position=0, money=0):
        self.gas = gas
        self.position = position
        self.money = money

    def getGas(self):
        return None
    
    #TODO other get/set functions

    '''
        trips is a list of Trip elements (the type above or an array)
        capacity is the number of seats in the vehicle
    '''
    def travel(self, trips, capacity) -> None:
        return

    def onlyGoingForward(self, trips, capacity: int) -> bool:
        return False

    def minDistance(self, trips, capacity) -> int:
        return 0

    # double underscores make a python function private
    def __gasCost(self, distance) -> int:
        return 0
    
    def __revenue(self, distance) -> int:
        return 0

    def totalProfit(self, trips, capacity) -> int:
        return 0
