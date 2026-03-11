import random

# RED - Veil of the Infernal Pact
# Temptation offers forbidden power, but poor decisions leave lingering corruption.
def questM1():

    print("\n=== Veil of the Infernal Pact ===")
    print("A whisper coils around your thoughts, offering power not meant for mortals.")
    print("You feel your life force pulse with each word.")
    print("\n1 - Accept the forbidden strength")
    print("2 - Refuse the whisper")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        # Skill check: player must type a "ritual word" correctly to channel the power safely
        ritual = input("To control the power, type the word that echoes in your mind: ").strip().lower()
        correct_word = random.choice(["ignite", "bind", "veil"])
        
        if ritual == correct_word:
            print("\nYour mind channels the infernal energy perfectly.")
            print("You gain temporary strength without corruption.")
            return True
        else:
            print("\nThe power twists inside your veins.")
            print("You gain strength, but a lingering curse reduces your max health by 10% for the next encounter.")
            return False

    elif choice == "2":
        print("\nYou resist the whisper, but the demon’s gaze leaves a lingering chill.")
        print("Your will remains intact, but your next skill check will be slightly harder (-5 to your roll).")
        return True

    return False