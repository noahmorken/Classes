class User:
    """A simple storage of basic user information."""

    def __init__(self, first_name, last_name, age, gender):
        """Initialize name and age attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Describes the user's basic information."""
        print(f"User: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        """Greets the user."""
        print(f"Hello, {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increases the number of login attempts made by one."""
        self.login_attempts += 1
        if self.login_attempts == 1:
            print(f"{self.first_name.title()} {self.last_name.title()} has made 1 login attempt.")
        else:
            print(f"{self.first_name.title()} {self.last_name.title()} has made {self.login_attempts} login attempts.")

    def reset_login_attempts(self):
        """Sets the number of login attempts made to zero."""
        self.login_attempts = 0
        print(f"{self.first_name.title()} {self.last_name.title()}'s login attempts have been reset.")


class Privileges:
    """Represents unique abilities of an administrator."""

    def __init__(self, privileges=['add posts', 'delete posts', 'ban users']):
        """Initialize the admin's privileges."""
        self.privileges = privileges

    def show_privileges(self):
        print("Administrators are authorized to preform the following actions:")
        for privilege in self.privileges:
            print(f"-{privilege.title()}")


class Admin(User):
    """Represents unique abilities of an administrator."""

    def __init__(self, first_name, last_name, age, gender):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()


first_user = User('George', 'Washington', 67, 'M')
second_user = User('Thomas', 'Jefferson', 83, 'M')
third_user = User('Abraham', 'Lincoln', 56, 'M')
fourth_user = User('Theodore', 'Roosevelt', 60, 'M')
fifth_user = Admin('John', 'Doe', 58, 'M')

print("\n")
first_user.describe_user()
first_user.greet_user()
first_user.reset_login_attempts()

print("\n")
second_user.describe_user()
second_user.greet_user()
second_user.increment_login_attempts()
second_user.reset_login_attempts()

print("\n")
third_user.describe_user()
third_user.greet_user()
third_user.increment_login_attempts()
third_user.increment_login_attempts()
third_user.reset_login_attempts()

print("\n")
fourth_user.describe_user()
fourth_user.greet_user()
fourth_user.increment_login_attempts()
fourth_user.increment_login_attempts()
fourth_user.increment_login_attempts()
fourth_user.reset_login_attempts()

print("\n")
fifth_user.describe_user()
fifth_user.greet_user()
fifth_user.increment_login_attempts()
fifth_user.increment_login_attempts()
fifth_user.increment_login_attempts()
fifth_user.increment_login_attempts()
fifth_user.reset_login_attempts()
fifth_user.privileges.show_privileges()