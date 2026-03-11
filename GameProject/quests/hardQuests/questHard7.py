import random

# Quest Name: The Hidden Number
# Description: A concealed number holds the key to passage.
#              Fail to guess it and a mysterious backlash weakens you.

def questH7():
    secret = random.randint(10, 20)
    print("\nA concealed number holds the key to passage.")
    guess = int(input("Guess the hidden number between 10 and 20: "))

    if guess == secret:
        print("Exact match! The hidden energy favors you.")
        return True
    else:
        print(f"Wrong! The hidden number was {secret}. A backlash weakens your next attempt.")
        return False