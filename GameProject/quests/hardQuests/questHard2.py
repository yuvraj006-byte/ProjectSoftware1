import random

# Quest Name: Shadow's Bargain   
# Description: A towering shadow stretches across the ruins.
#              Accept its offered strength, but beware the hidden corruption.  

def questH2():
    print("\nA towering shadow stretches across the ruins.")
    print("'I can double your strength… but nothing is free.'\n")
    print("1 - Accept immediately")
    print("2 - Ask the price")
    print("3 - Refuse")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        chance = random.randint(1, 100)
        if chance <= 40:
            print("You withstand the corruption. Power surges through you.")
            return True
        else:
            print("The shadow overwhelms you! You are cursed and weaker for the next quest.")
            return False
    elif choice == "2":
        print("You learn the cost and survive the exchange, but some power is withheld.")
        return True
    elif choice == "3":
        print("You walk away unharmed, but nothing is gained.")
        return False

    return False