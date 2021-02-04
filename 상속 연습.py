class car():
    def __init__(self, speed):
        self.__speed = speed
    def setSpeed(self):
        self.__speed = speed
    def getSpeed(self):
        return self.__speed

class sportscar(car):
    def __init__(self, speed, turbo):
        super().__init__(speed)
        self.__turbo = turbo
    def setTurbo(self):
        self.__turbo = turbo


