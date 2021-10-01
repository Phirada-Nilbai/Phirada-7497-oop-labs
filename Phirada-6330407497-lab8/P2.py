#Phirada Nilbai 633040749-7 P2
class Vehicle:

    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage


    def set_speed(self,speed):
        self.speed = speed


class Car(Vehicle):
    def __init__(self, name, mileage, speed,num_doors):
        self.name = name
        self.mileage = mileage
        self.speed = speed
        self.num_doors = num_doors
        super().__init__(name, mileage,speed)


    def __str__(self):
        return (f"NAME:{self.name} speed:{self.speed} mileage:{self.mileage} num doors:{self.num_doors}")


class Bus(Vehicle):
    def __init__(self, name, mileage, speed,capacity):
        self.name = name
        self.mileage = mileage
        self.speed = speed
        self.capacity = capacity
        super().__init__(name, mileage, speed)


    def __str__(self):
        return (f"NAME:{self.name} speed:{self.speed} mileage:{self.mileage} num doors:{self.capacity}")


if __name__ == '__main__':
    car = Car("Toyota Vios",90 , 150000 , 4)
    bus = Bus("School Volvo" ,12 , 200000 , 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)
