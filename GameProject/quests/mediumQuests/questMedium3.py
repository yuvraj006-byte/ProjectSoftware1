# RED - Gate of the Night Sovereign
# Must interpret the riddle and type correct symbol.
def questM3():

    print("\n=== Gate of the Night Sovereign ===")
    print("An iron gate looms before you.")
    print("Carved above it are four symbols: Sun  Moon  Star  Crown")
    print("\nInscription: 'Only that which rules the night may pass.'")

    answer = input("Speak the ruling symbol: ").strip().lower()

    if answer == "moon":
        print("\nThe gate groans open with a thunderous echo.")
        return True
    else:
        print("\nThe mechanism jams and strikes you with an electric shock!")
        print("You are stunned and your next strength-based action is halved.")
        return False