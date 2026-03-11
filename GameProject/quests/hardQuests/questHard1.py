import random

# Quest Name: Sanctuary of Chaotic Power
# Description: A fractured Sanctuary core pulses with unstable, chaotic energy.
#              Channel it wisely or risk being shredded by raw power.

def questH1():
    print("\nA fractured Sanctuary core pulses with unstable, chaotic energy.")
    print("Low  - Light touch (safe, minor power)")
    print("Medium - Channel briefly (moderate risk, moderate gain)")
    print("High - Absorb fully (great risk, high reward)")

    choice = input("Choose risk (low / medium / high): ").lower()
    
    if choice == "low":
        chance = 40
        penalty = "Minor shock drains stamina."
    elif choice == "medium":
        chance = 60
        penalty = "Backlash bruises your body, reducing your next attack."
    elif choice == "high":
        chance = 75
        penalty = "Severe energy backlash injures you, lowering health significantly."
    else:
        print("Invalid choice. The energy recoils harmlessly.")
        return False

    roll = random.randint(1, 100)

    if roll <= chance:
        print("The energy bends to your will. You gain its power.")
        return True
    else:
        print("The energy lashes back violently! " + penalty)
        return False