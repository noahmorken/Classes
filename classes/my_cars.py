# from car import Car, ElectricCar
# from car import *
# import car
from car import Car
from electric_car import ElectricCar as EC

# my_beetle = car.Car('volkswagen', 'beetle', 2019)
my_beetle = Car('volkswagen', 'beetle', 2019)
print(f"\n{my_beetle.get_descriptive_name()}")

# my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
my_tesla = EC('tesla', 'roadster', 2019)
print(f"\n{my_tesla.get_descriptive_name()}")