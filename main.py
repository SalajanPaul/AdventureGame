import random


def AdventureGame():
    bonus_options = ["hp", "damage"]
    bonus_hp = 25
    bonus_damage = 50
    bonus = random.choices(bonus_options)

    player_health = 250
    enemies = [
        {"name": "wolf", "health": 100, "damage": 20},
        {"name": "bear", "health": 100, "damage": 25},
        {"name": "dragon", "health": 200, "damage": 30}
    ]

    character_name = input("What is your character name? ")

    character_weapon = input("What weapon will you like to pick: sword, axe or mace ")

    weapon_damage = {"sword": 25, "axe": 30, "mace": 45}.get(character_weapon, 25)

    print(f" ////// Hello {character_name}, your weapon will be a {character_weapon}! //////")

    for enemy in enemies:
        enemy_name = enemy["name"]
        enemy_health = enemy["health"]

        print(f"You encountered a {enemy_name}")

        while player_health > 0 and enemy_health > 0:
            # Player's turn
            enemy_health -= weapon_damage
            print(f"{enemy_name} health: {enemy_health}")

            # Enemy's turn
            player_health -= enemy["damage"]
            print(f"Your health remaining: {player_health}")


        if player_health <= 0:
            print("You died!")
            break

        print(f"You defeated {enemy_name}!")

    print("Congratulation, you won!")




AdventureGame()
