# Quest Name: Trial of the Statues of Mezanod
# Description: Four statues present a logic puzzle.
#              Deduce their correct order or the puzzle resets, draining your focus. 


def questH10():
    print("\nFour statues stand in a line: Warrior, Mage, Beast, King.")
    print("'The Beast stands after the Mage.'")
    print("'The Warrior is not at either end.'")
    print("'The King stands at one of the ends.'")
    print("Who stands in the second position?")

    answer = input("Your answer: ").strip().lower()

    if answer == "warrior":
        print("The statues shift, acknowledging your reasoning.")
        return True
    else:
        print("The puzzle resets, draining your focus for the next challenge.")
        return False