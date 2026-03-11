# Quest Name: Fusion of Spirit Fragments
# Description: Four spirit fragments grant power, but miscalculating their fusion shatters them violently, leaving you weakened.


def questH4():
    print("\nEach spirit fragment grants 6 power.")
    print("You collect 4 fragments.")
    print("Channeling costs 5 power.")
    print("Calculate the remaining power carefully:")

    answer = input("Your answer: ")

    if answer.strip() == "19":
        print("The fragments fuse seamlessly into your core.")
        return True
    else:
        print("The fragments shatter violently, leaving you weakened for future trials.")
        return False