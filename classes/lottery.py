import random

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
winning_combo = ""
my_ticket = ""
num_attempts = 1

for combination in range(0, 4):
    character = random.choice(characters)
    my_ticket += character

while winning_combo != my_ticket:
    winning_combo = ""
    for combination in range(0, 4):
        character = random.choice(characters)
        winning_combo += character
    num_attempts += 1

print(f"Any ticket matching with {winning_combo} wins a prize!")

if num_attempts == 1:
    print(f"Wow, you got a winning ticket on your first try!")
else:
    print(f"You got a winning ticket in {num_attempts} attempts.")