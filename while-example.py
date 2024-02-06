import random

lives = 3
while lives > 0:
    print("You have", lives, "lives left.")
    dice = random.randint(1, 6)
    print("You rolled a", dice)
    if dice == 6:
        print("\n\nYOU WIN!\n\n")
        break
    else:
        lives = lives - 1
print("Thank you for playing. Goodbye.")
