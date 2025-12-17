# Ashley Rowland
#Bellevue University- CSD325
# chohan_ar.py
# Updated according to Module 3 assignment instructions
# Changes made:
# - Updated input prompt to use initials
# - House percentage changed from 10% → 12%
# - Added rule: Roll of 2 or 7 gives a 10 mon bonus
# - Added program intro message explaining bonus
# - Added logic to apply +10 bonus to purse
# - Added message telling user they earned the bonus

import random

print("Welcome to the game of Cho-Han!")
print("Roll a 2 or 7 and you earn a 10 mon bonus!\n")

purse = 100

while purse > 0:
    print(f"Current purse: {purse} mon")
    bet = int(input("yr: "))   # Example initials: yr:

    # Roll dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"You rolled {die1} and {die2}. Total = {total}")

    # Bonus rule for 2 or 7
    if total == 2 or total == 7:
        print("Bonus! You rolled a lucky number (2 or 7). +10 mon added!")
        purse += 10

    # Player guess
    guess = input("Do you guess Even or Odd? (e/o): ").lower()

    # Determine outcome
    result = "even" if total % 2 == 0 else "odd"

    # Win or lose
    if (guess == "e" and result == "even") or (guess == "o" and result == "odd"):
        print("You won the round!")
        purse += bet
    else:
        print("You lost the round!")
        purse -= bet

    # 12% house fee
    house_fee = int(purse * 0.12)
    purse -= house_fee
    print(f"House fee (12%): {house_fee} mon")

    # Continue?
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break

print("\nThanks for playing Cho-Han!")
print(f"Final purse: {purse} mon")