import random


def AdventureGame():
    player_health = 100
    wolf_health = 100
    wolf_damage = 20
    bear_health = 100
    bear_damage = 25
    dragon_boss_health = 100
    dragon_boss_damage = 45

    character_name = input("What is your character name? ")

    sword_damage = 25
    axe_damage = 30
    mace_damage = 45

    character_weapon = input("What weapon will you like to pick: sword, axe or mace ")

    print(f" ////// Hello {character_name}, your weapon will be {character_weapon}! //////")

    while player_health > 0:
        # first enemy wolf #
        if character_weapon == "sword":
            player_health -= wolf_damage
            print("Your health:", player_health)
            wolf_health -= sword_damage
            if wolf_health <= 0:
                print(f"You won! Remaining health: {player_health}")
                # second enemy bear #
                player_health -= bear_damage
                print("Your health:", player_health)
                bear_health -= sword_damage
            if player_health <= 0:
                print("You lost")
                break



AdventureGame()



