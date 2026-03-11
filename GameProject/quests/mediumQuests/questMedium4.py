import random
# RED - Trial by Infernal Might
# Strength duel with skill + randomness; penalty for failure.
def questM4():

    print("\n=== Trial by Infernal Might ===")
    print("A horned lesser demon steps forward, cracking its knuckles.")
    print("Choose your strength wisely (10–20). Rolling too low will make you vulnerable!")

    try:
        player = int(input("Enter your attack number: "))
    except:
        print("Hesitation is weakness. The demon strikes first!")
        return False

    demon = random.randint(12, 22)
    roll_modifier = random.randint(-2, 2)
    demon += roll_modifier

    print("\nYou unleash:", player)
    print("The demon counters with:", demon)

    if player > demon:
        print("Your blow overpowers the fiend. You stand victorious.")
        return True
    else:
        print("The demon’s strike overpowers you.")
        print("You lose some health and must rest before the next challenge (-10 HP).")
        return False