import random

# Quest Name: Endurance of the Shadows
# Description: Three shadow strikes aim to break your resolve. Collapse and recovery will be slow.

def questH6():
    print("\nThree shadow strikes aim to break your resolve.")
    health = 30

    for i in range(3):
        damage = random.randint(8, 15)
        health -= damage
        print(f"Strike {i+1} deals {damage} damage. Remaining health: {max(health,0)}")
        if health <= 0:
            print("You collapse under the assault. Recovery will be slow.")
            return False

    print("You endure the shadows. Your stamina is tested but intact.")
    return True