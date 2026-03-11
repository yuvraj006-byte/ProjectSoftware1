import random

# Quest Name: The Astral Wager of Unnulaaz
# Description: The Demon Lord Unnulaaz does not walk the mortal plane—
#              his astral will bends fate itself. Accept his unseen wager.
#              Call the coin correctly, or his thralls will answer in his stead.

def questE4():
    coin_toss = ["heads", "tails"]

    print("\n=== The Astral Wager of Unnulaaz ===")
    print("The air grows cold. Shadows stretch unnaturally across the ground.")
    print("A whisper echoes inside your mind—not from this realm.")
    print('"I do not need a body to break you..."')
    print("Unnulaaz, Demon Lord of the Red Veil, watches from the astral abyss.")
    print("Before you, a coin forms from condensed shadow.")
    print("Call it correctly… or his servants shall manifest.\n")

    while True:
        choice = input("Choose your fate: Heads or Tails? ").strip().lower()

        if choice in coin_toss:
            break
        print("The whisper tightens around your thoughts. Speak: 'heads' or 'tails'.")

    print("\nThe shadowed coin rises without touch...")
    print("It spins, distorting the air around it...")
    
    demon_choice = random.choice(coin_toss)

    print("Time fractures for a heartbeat...")
    print(f"It falls upon: {demon_choice.upper()}!\n")

    return choice == demon_choice


def questE4_result():
    if questE4():
        print("The shadows recoil violently.")
        print("A distant, enraged howl echoes from the astral plane.")
        print("Unnulaaz's influence fades—for now.")
        print("Quest Complete: You resisted the Astral Wager.")
        print("Reward: 120 Gold and 200 XP.")
    else:
        print("The coin dissolves into black mist.")
        print("A rift tears open beside you...")
        
        summoned = random.choice([
            "Imp",
            "Hell Hound",
            "Blood Thrall",
            "Soul Drinker"
        ])

        print(f"Unnulaaz does not appear himself.")
        print(f"Instead, he sends forth a {summoned} to claim what is owed!")
        print("Prepare for combat!")
        print("\nQuest Failed: The Astral Wager turns against you.")