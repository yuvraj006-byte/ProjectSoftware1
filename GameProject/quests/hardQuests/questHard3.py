# Quest Name: Riddle of the Unseen
# Description: An abstract riddle of unseen forces tests your insight.
#              Name the invisible threat or suffer phantom strikes.

def questH3():
    print("\nI have no blade, yet I can cut.")
    print("I have no hands, yet I can break.")
    print("The strongest warrior fears me.")
    print("What am I?")

    answer = input("Your answer: ").strip().lower()

    if answer == "fear":
        print("The darkness acknowledges your insight. You may proceed unscathed.")
        return True
    else:
        print("You fail to name the unseen force. A phantom strike wounds you for the next challenge.")
        return False