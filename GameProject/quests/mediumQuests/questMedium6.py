import random

# RED - The Crimson-Eyed Survivor
# Choice + chance with consequences if corrupted.
def questM6():

    print("\n=== The Crimson-Eyed Survivor ===")
    print("A wounded figure crawls from the ruins. Their eyes shimmer faintly red.")
    print("\n1 - Help them rise")
    print("2 - Keep your distance")

    choice = input("Choose 1 or 2: ").strip()

    if choice == "1":
        chance = random.randint(1, 100)

        if chance <= 40:
            print("\nTheir grip tightens unnaturally, spreading corruption!")
            print("You take -5 health and -2 to your next skill roll.")
            return False
        else:
            print("\nTheir eyes clear. You have saved a soul from the brink.")
            return True
    elif choice == "2":
        print("\nYou step back cautiously. Not all suffering is innocent.")
        return True

    return False