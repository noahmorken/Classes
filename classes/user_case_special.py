from users import User

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