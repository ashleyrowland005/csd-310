# Author: Ashley Rowland
#Date: 12-7-25
# Assignment: Module 1 - On the Wall
# Description: Asks user for number of bottles, counts down with correct lyrics,
# then reminds user to buy more beer.

def countdown(bottles):
    # Loop until we reach 1 bottle
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall...")
        bottles -= 1

    # Handle the 1 bottle case separately
    print("1 bottle of beer on the wall...")

# ---------------- MAIN PROGRAM ---------------- #

# Ask the user for input
num_bottles = int(input("How many bottles of beer are on the wall? "))

# Call the function
countdown(num_bottles)

# Final message
print("Time to buy more beer!")