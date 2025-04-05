name = input("Enter your name: ")  # string
money = input("Enter your cash amount: ")  # string
hunger = input("Are you hunger? (Y/N) ")  # string

if hunger == "Y":
    if int(money) >= 30:
        print(f"{name} should go eat breakfast.")
    else:
        print(f"{name} is hungry but might not have enough money to buy breakfast.")
elif hunger == "N":
    if int(money) >= 30:
        print(f"{name} has budget but doesn't want to eat breakfast.")
    else:
        print(f"{name} has no money but is not hunger...")
else:
    print("Please make sure you enter Y or N.")
