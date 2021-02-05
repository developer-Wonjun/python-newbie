class Vehicle():
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        return "운전"
    def stop(self):
        return "정지"

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
    
    def drive(self):
        return "승용차를 운전합니다."
    
    def stop(self):
        return "승용차가 정지합니다."

class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
        return "트럭을 운전합니다."
    
    def stop(self):
        return "트럭이 정지합니다."


cars = [Truck("truck1"), Truck("truck2"), Car("car1")]

for car in cars:
    print(car.name + ":" + car.drive())

