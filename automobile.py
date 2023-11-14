
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def main():
    vehicle_type = "car"  
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4) of the car: ")
    roof = input("Enter the type of roof (solid or sun roof) of the car: ")

    automobile = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nVehicle type: " + automobile.vehicle_type)
    print("Year: " + automobile.year)
    print("Make: " + automobile.make)
    print("Model: " + automobile.model)
    print("Number of doors: " + automobile.doors)
    print("Type of roof: " + automobile.roof)


if __name__ == "__main__":
    main()
