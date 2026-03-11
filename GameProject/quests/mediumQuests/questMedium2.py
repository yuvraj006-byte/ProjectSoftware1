# RED - The Frostbound Seal
# Must interpret a hint and input a sequence of runes correctly.
def questM2():

    print("\n=== The Frostbound Seal ===")
    print("A colossal stone door blocks your path, pulsating with arcane energy.")
    print("Three runes blaze upon its surface:")
    print("1 - Flame Rune")
    print("2 - Frost Rune")
    print("3 - Storm Rune")
    print("\nHint engraved faintly in frost: 'Only cold can calm rising flame.'")

    # Player must input sequence correctly
    sequence = input("Choose the correct sequence of runes by number (e.g., '2'): ").strip()

    if sequence == "2":
        print("\nThe frost rune pulses softly.")
        print("The raging magic settles into silence. Door opens.")
        return True
    else:
        print("\nThe runes flare violently!")
        print("A burst of energy scorches you, reducing your next attack by 2 points.")
        return False