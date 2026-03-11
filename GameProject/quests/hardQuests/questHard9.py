# Quest Name: Silence of the Void
# Description: A riddle of absence and silence. Solve it or have the void drain your willpower.

def questH9():
    print("\nI am taken before you can see me.")
    print("I vanish the moment I am said.")
    answer = input("Your answer: ").strip().lower()

    if answer == "silence":
        print("Correct. The void respects your understanding.")
        return True
    else:
        print("Incorrect. The void remains unbroken and drains your willpower.")
        return False