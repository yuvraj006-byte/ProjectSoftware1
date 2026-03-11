import random

# Quest Name: Duel with the Void Guardian
# Description: Face a powerful guardian.
#              Outroll its strength by at least 3 points or be struck and wounded. 

def questH8():
    print("\nA guardian of immense strength stands before you.")
    print("Choose your attack strength (15–30).")

    player = int(input("Enter your attack number: "))
    guardian = random.randint(20, 35)

    print(f"You roll: {player} | Guardian rolls: {guardian}")

    if player >= guardian + 3:
        print("You overwhelm the guardian and stand victorious.")
        return True
    else:
        print("You are struck and wounded. Your combat ability is temporarily reduced.")
        return False