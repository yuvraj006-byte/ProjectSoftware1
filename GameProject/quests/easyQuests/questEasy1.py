import random

# Quest Name: The Crucible of Calculated Will
# Description: An unseen intellect presses against your mind.
#              Prove your discipline, or your thoughts will fracture.

def questE1():
    a = random.randint(12, 100)
    b = random.randint(12, 100)

    print("\n=== The Crucible of Calculated Will ===")
    print("A cold pressure grips your skull.")
    print("An astral presence tests the strength of your mind.")
    print("Numbers burn into your vision...\n")

    try:
        answer = int(input(f"What is {a} x {b}?: "))
    except:
        print("Your hesitation fractures your focus.")
        return False

    if answer == a * b:
        print("\nThe pressure fades.")
        print("Your mind remains unbroken.")
        return True
    else:
        print(f"\nThe correct answer was {a * b}.")
        print("The presence tightens briefly—feeding on your lapse.")
        return False


def questE1_result():
    if questE1():
        print("Quest Complete: The Crucible yields.")
        print("Reward: 90 Gold, 150 XP.")
    else:
        print("Quest Failed: Your will falters.\nNo reward.")