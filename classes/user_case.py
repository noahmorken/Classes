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