import random

# RED - The Fork of Ashen Fate
# Random path choice, wrong choice reduces stamina or chance in next challenge.
def questM7():

    print("\n=== The Fork of Ashen Fate ===")
    print("The forest is silent. Two paths stretch before you, swallowed in red mist.")

    path = input("Choose 'left' or 'right': ").strip().lower()
    safe_path = random.choice(["left", "right"])

    if path == safe_path:
        print("\nThe mist thins as you proceed. You move safely forward.")
        return True
    else:
        print("\nThe trees close in. Something unseen scratches at you.")
        print("You lose stamina (-5 HP) and your next dexterity roll is harder.")
        return False