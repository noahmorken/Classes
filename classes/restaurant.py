class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes information about a restaurant."""
        print(f"{self.restaurant_name} is a resaurant that serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Simulate a restaurant opening."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, served):
        """
        State the number of customers a restaurant has served.
        Reject the change if it tries to roll the number back.
        """
        if served >= self.number_served:
            self.number_served = served
            print(f"{self.restaurant_name} has served {self.number_served} customers.")
        else:
            print("You can't unserve a customer!")

    def increment_number_served(self, served):
        """
        Add the given amount to the number of customers served.
        Reject the change if it tries to roll the number back.
        """
        if served >= 0:
            self.number_served += served
            print(f"{self.restaurant_name} has served {self.number_served} customers.")
        else:
            print("You can't unserve a customer!")


class IceCreamStand(Restaurant):
    """Represents unique aspects of an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def list_flavors(self):
        print("The ice cream stand serves the following flavors:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")


first_restaurant = Restaurant('Freddy\'s', 'American')
second_restaurant = Restaurant('Corona\'s', 'Mexican')
third_restaurant = Restaurant('Go Fish', 'Japanese')
fourth_restaurant = IceCreamStand('Dreyer\'s', 'French')

print("\n")
first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()
first_restaurant.set_number_served(10)
first_restaurant.increment_number_served(40)

print("\n")
second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()
second_restaurant.set_number_served(15)
second_restaurant.increment_number_served(35)

print("\n")
third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()
third_restaurant.set_number_served(20)
third_restaurant.increment_number_served(30)

print("\n")
fourth_restaurant.describe_restaurant()
fourth_restaurant.open_restaurant()
fourth_restaurant.set_number_served(25)
fourth_restaurant.increment_number_served(25)
fourth_restaurant.list_flavors()