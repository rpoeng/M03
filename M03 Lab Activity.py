#Robert K Poeng
#M03 Lab - Case Study: Lists, Functions, and Classes 

#Specifications 
# 1.) Needs a super class called 'Vehicle', which contains attributes for vehicle type such as
# Car, Truck, Plane, Boat or for some odd reason a broomstick. Witches be Witches I guess.

# 2.) A Class called 'Automobile' which will inherit attributes from vehicle and also contain the following
# year, make, model, door (2 or 4), roof (solid or sun roof).

#Object Oriented Code

#Convention naming for class, they should be capitalized
class Vehicle:
    #vehicle_type
    # ' ' between def & __init__
    def __init__(self):#Also know as the constructor. (Short for intialize) 
        self.vehicle_type = None


class Automobile(Vehicle):

    #year = None
    #make = None
    #model = None
    #door = None
    #roof = None

    def __init__(self,year,make,model,door,roof): #Also know as the constructor. (Short for intialize) 
        self.year = None
        self.make = None
        self.model = None
        self.door = None
        self.roof = None