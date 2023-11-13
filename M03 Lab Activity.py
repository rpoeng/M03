#Robert K Poeng
#M03 Lab - Case Study: Lists, Functions, and Classes 

#Specifications 
# 1.) Needs a super class called 'Vehicle', which contains attributes for vehicle type such as
# Car, Truck, Plane, Boat or for some odd reason a broomstick. Witches be Witches I guess.

# 2.) A Class called 'Automobile' which will inherit attributes from vehicle and also contain the following
# year, make, model, door (2 or 4), roof (solid or sun roof).

#Object Oriented Code
#Classes are basically blueprints for creating objects.

#Convention naming for class, they should be capitalized
class Vehicle:
    #vehicle_type = None
    # ' ' between def & __init__
    def __init__(self,vehicle_type):#Also know as the constructor. (Short for intialize) 
        self.vehicle_type = vehicle_type #'self' refers to the object we are currently working on.


class Automobile(Vehicle): # This will refer to the super class "Vehicle" and calls it when needed.
    #year = None
    #make = None
    #model = None
    #door = None
    #roof = None

    def __init__(self,vehicle_type, year,make,model,door,roof): 
        #self.vehicle_type = vehicle_type
        super().__init__(vehicle_type) # gets the definition from the parent class "Vehicle"
        self.year = year
        self.make = make
        self.model = model
        self.door = door
        self.roof = roof

    def vehicle_information(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.door)
        print("Type of roof:", self.roof)

def user_input():
    vehicle_type = input("Vehicle type: ")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    door = input("Number of doors: ")
    roof = input("Type of roof: ")

    return vehicle_type, year, make, model, door, roof
