# used to model a real life object
# objects have parameters(attributes;colour,breed): function(actions)
#this is a class used to identify a car

class car:
    def __init__(self ,model,make,year_of_production ,fuel_capacity,colour):
       self.model =model
       self.make =make
       self.year_of_production =year_of_production 
       self.fuel_capacity =fuel_capacity 
       self.colour =colour

    def print_make(self,make):
       print("The car is of {0} make" .format(self.make))

    def set_make(self,make):
       self.make=make
    def get_make(self):
       return self.make
    def set_colour(self,colour):
       self.colour =colour
    def get_colour (self):
       return self.colour

    def set_model(self,model):
       self.model=model
    def get_model(self):
       return self.model   

    

my_car =car("Impala","Chevolet","1969","2500cc","lilac")

my_car.print_make("Chevolet")
my_car.set_make("Ford")
print(my_car.get_make())

my_car.set_colour("Pink")
print(my_car.get_colour())

my_car.set_model("nissan")
print(my_car.get_model())