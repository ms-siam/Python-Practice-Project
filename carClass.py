class Car:
    def __init__(self, make, model, year):
        # Initialize attributes here
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def describe(self):
        # Print car details here
        print(f"{self.year} {self.make} {self.model}")
    def updateMileage(self, newMileage):
        if newMileage >= self.mileage:
            self.mileage = newMileage
        else:
            print('Mileage cannot be decreased')
    def displayMileage(self):
        print(f"Current Mileage:{self.mileage} miles")

Car1 = Car("Toyota", "Corolla", 2015)
Car1.describe()
Car.updateMileage(Car1,15000)
Car.displayMileage(Car1)