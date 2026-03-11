# RED - Temptation of the Gilded Snare
# Resist greed or take damage and temporary curse if you fail.
def questM5():

    print("\n=== Temptation of the Gilded Snare ===")
    print("A radiant chest hums with unnatural light. Its glow feels wrong.")
    print("\nType 'open' to open it or anything else to walk away.")

    action = input("Your decision: ").strip().lower()

    if action != "open":
        print("\nYou turn away. The light dims behind you.")
        print("You remain unscathed, but curiosity gnaws at you. (+5 tension for next encounter)")
        return True
    else:
        print("\nThe chest snaps open! Dark sigils coil around your wrist.")
        print("You are cursed: -5 to all rolls for the next challenge.")
        return False