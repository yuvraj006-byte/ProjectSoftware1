# Quest Name: Murmur of the Veilbound Shade
# Description: A drifting shade whispers a riddle from the edge of the light.

def questE2():

    print("\n=== Murmur of the Veilbound Shade ===")
    print("A translucent figure flickers at the corner of your sight.")
    print("Its voice is barely audible—like wind through a crypt.\n")

    print("I am born at your feet in the sun,")
    print("I stretch long when the day is done,")
    print("But in deepest night, I am gone.\n")

    answer = input("What am I? ").strip().lower()

    return answer == "shadow"


def questE2_result():
    if questE2():
        print("\nThe shade bows silently and dissolves into mist.")
        print("Quest Complete: The riddle is answered.")
        print("Reward: 70 Gold, 120 XP.")
    else:
        print("\nThe shade shrieks softly and fades.")
        print("Quest Failed: The whisper was lost to you.")