# Every time the game is run, the dog will be assigned to a room location randomly.The user will be given a list of rooms to pick from until the dog is found. When the mission is complete, the user recieves a congratulation message. However, if the user guesses wrong, they will be asked to try again.

import random
#rooms to pick from
rooms = (" KITCHEN", " BATHROOM", " OFFICE", " DEN", " BASEMENT", " CLOSET")
dog = random.choice(rooms)
print("You are doing your homework when you hear your dog whimpering from somewhere downstairs. Figuring that he accidentally locked himself out when running out the back door, but he wasn't outside. It's now your mission to find him before your parents come home.")
print("Directions:")
print("When prompted, choose a room from the list to check in first. Continue searching through the house until you find him. But remember: he may never hide in the same place twice.")
print("Choose a room: kitchen, bathroom, closet, den, basement, or office.")

while True:
    rooms = (" KITCHEN", " BATHROOM", " OFFICE", " DEN", " BASEMENT", " CLOSET")
    dog = random.choice(rooms)
    guess = input("Please choose a direction")
    guess = guess.upper()
    if guess in dog:
        print("Congratulations! You found the good boy!")
        break
    else:
        print("Please guess again.")
