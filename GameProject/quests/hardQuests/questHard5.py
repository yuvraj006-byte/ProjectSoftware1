# Quest Name: Word of True Might
# Description: Speak a word of power meeting strict conditions. Weak words are consumed by darkness and sap your strength.


def questH5():
    print("\nSpeak a word of immense power.")
    print("Conditions: Longer than 6 letters and at least 2 vowels.")

    word = input("Your word: ").lower()
    vowels = sum(1 for c in word if c in "aeiou")

    if len(word) > 6 and vowels >= 2:
        print("The word resonates with potent energy.")
        return True
    else:
        print("The word falters and is absorbed by the darkness. You feel drained.")
        return False