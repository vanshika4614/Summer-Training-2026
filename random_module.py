# Day 7 - Random Module

import random

# Generate a random integer
print("Random Integer:", random.randint(1, 10))

# Generate a random float
print("Random Float:", random.random())

# Random choice from a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Random Fruit:", random.choice(fruits))

# Shuffle a list
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print("Shuffled List:", numbers)

print()

# -------------------------------
# Stone Paper Scissors Game
# -------------------------------

choices = ["stone", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter Stone, Paper or Scissors: ").lower()

print("Computer Chose:", computer)

if user not in choices:
    print("Invalid Input")

elif user == computer:
    print("Match Draw")

elif (user == "stone" and computer == "scissors") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissors" and computer == "paper"):
    print("You Win!")

else:
    print("Computer Wins!")