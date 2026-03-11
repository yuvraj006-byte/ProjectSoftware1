# Quest Name: Severing the Lesser Flame
# Description: A flame-bound lesser demon stalks the ruins.
#              Choose its weakness wisely before it strikes.

def questE5():

    print("\n=== Severing the Lesser Flame ===")
    print("A smoke-wreathed Lesser Demon crawls from a fissure in the earth.")
    print("Its claws burn with cursed fire.")
    print("You must exploit its weakness before battle begins.\n")

    print("1 - A blade of Silver blessed by moonlight")
    print("2 - A vial of Dragon's Blood")
    print("3 - A Tome of Ancient Fire\n")

    choice = input("Choose 1, 2, or 3: ")

    return choice == "1"


def questE5_result():
    if questE5():
        print("\nThe silver flashes.")
        print("The demon shrieks as its flame collapses inward.")
        print("Quest Complete: The lesser spawn is undone.")
        print("Reward: 110 Gold, 160 XP.")
    else:
        print("\nYour choice fails to pierce its infernal nature.")
        print("The demon retreats into smoke, laughing.")
        print("Quest Failed: No reward.")