# Structural Pattern Matching
# switch statement ==

command = input("Where do you wanna go? ")

match command.split(" "):
    case ["Go", "north"]:
        print("You are heading to the north.")
    case ["Go", "east"]:
        print("You are heading to the east.")
    case ["Go", "west"]:
        print("You are heading to the west.")
    case ["Go", "south"]:
        print("You are heading to the south.")
    case ["Turn", "left"]:
        print("You want to turn Left.")
    case ["Turn", "right"]:
        print("You want to turn Right.")
    case _:
        print("I dont understand what you want to do.")
