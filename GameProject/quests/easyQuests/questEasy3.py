# Quest Name: The Veiled Sigil of Salvation
# Description: An altar conceals its intent within hidden structure.

def questE3():

    print("\n=== The Veiled Sigil of Salvation ===")
    print("An ancient altar hums with dormant power.")
    print("Four words are carved into blackened stone:\n")

    print("Silent")
    print("Ash")
    print("Voices")
    print("Eternal\n")

    print("A distant whisper murmurs:")
    print("'The first of each shall reveal the path...'\n")

    answer = input("What word is hidden? ").strip().lower()

    return answer == "save"


def questE3_result():
    if questE3():
        print("\nThe altar trembles violently.")
        print("A hidden chamber opens, revealing a faintly glowing amulet.")
        print("Quest Complete: The sigil is unveiled.")
        return True
    else:
        print("\nThe runes dim.")
        print("Quest Failed: The altar remains sealed.")
        return False