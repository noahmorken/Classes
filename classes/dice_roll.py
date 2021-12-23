from random import randint

class Die:
    """Simulates a dice roll."""

    def __init__(self, sides):
        """Initialize number of sides on dice."""
        self.sides = sides

    def describe_die(self):
        """Prints the number of sides the die has."""
        print(f"\nThis die has {self.sides} sides.")

    def roll_die(self):
        """Picks a random number between one and the number of sides, printing results."""
        result = randint(1, self.sides)
        print(f"You rolled a {result}.")


six_sided_die = Die(6)
six_sided_die.describe_die()
for rolls in range(0, 10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
ten_sided_die.describe_die()
for rolls in range(0, 10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)
twenty_sided_die.describe_die()
for rolls in range(0, 10):
    twenty_sided_die.roll_die()