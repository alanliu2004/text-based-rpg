from player import Player, Morality
import endings
import enemies


# Constants
EVIL = 'evil'
GOOD = 'good'
NEUTRAL = 'neutral'
INVALID = "Invalid Choice. Try Again"
game_on = True

# Assigns all the classes to variables
player = Player()
ending = endings.Ending()
goblin = enemies.Goblin()
skeleton = enemies.Skeleton()
slime = enemies.Slime()
demon_king = enemies.DemonKing()
moral = Morality()


# Combat System where it takes the player's health as the combat resource
def combat(enemy):
    global game_on
    # Ends the game if the player's health drops to 0
    if player.health <= enemy.attack:
        player.health -= enemy.attack
        ending.game_over()
        moral.display()
        game_on = False
        return
    else:
        player.health -= enemy.attack
        print(f'You took {enemy.attack} damage from the {enemy.name}. Health is now {player.health}')

# Game locations (branches)
def start_town():
    if not game_on:
        return
    choice = input('You see a woman being attacked by a goblin.\n[1] Save her (Enter Combat)\n[2] Run away\n')
    if choice == "1":
        moral.karma(GOOD)
        combat(goblin)
    elif choice == "2":
        moral.karma(EVIL)
    else:
        print(INVALID)
        start_town()

def leave_town():
    choice = input("You are now leaving for the Kingdom. Before you leave, A boy asks if you could spare some food for his family.\n[1] Ignore the boy and depart.\n[2] Leave some food for him and his family.\n")
    if not game_on:
        return
    if choice == '1':
        moral.karma(EVIL)
    elif choice == '2':
        moral.karma(GOOD)
        player.health_decrease(20)
    else:
        print(INVALID)
        leave_town()

def kingdom_arrival():
    if not game_on:
        return
    choice = input("You have arrived at the Kingdom. You are tasked with finding and saving the princess, but first, the king asks you if you could take care of some problems.\n[1] Help the King, but it will take some time.\n[2] Decline the king's request, and hurriedly set off.")
    if choice == '1':
        print("As a reward, you drink a health potion.")
        moral.karma(GOOD)
        player.health_increase(10)
        player.timer_increase()
    elif choice == '2':
        moral.karma(EVIL)
    else:
        print(INVALID)
        kingdom_arrival()

def forest():
    if not game_on:
        return
    choice = input("You found yourself in a forest, while your way to the Demon King's castle. There is a group of kids surrounded by skeletons.\n[1] Enter Combat.\n[2] The kids will save themselves.\n")
    if choice == '1':
        moral.karma(GOOD)
        combat(skeleton)
        combat(skeleton)
        combat(skeleton)
    elif choice == '2':
        moral.karma(EVIL)
    else:
        print(INVALID)
        forest()

def fairy():
    global game_on
    if not game_on:
        return
    choice = input("You found a forest fairy. It is offering to increase your max health, but in exchange, you lose health.\n[1] Take the offer.\n[2] Refuse the offer.\n")
    if choice == '1':
        player.max_health_increase(20)
        player.health_decrease(20)
        if player.health < 1:
            print("You have died.")
            game_on = False
    elif choice == '2':
        moral.karma(NEUTRAL)
    else:
        print(INVALID)
        fairy()

def lost_forest():
    if not game_on:
        return
    choice = input("Accidentally wondered off of the path and now you are lost in the forest. You hear a sound in the distance trees.\n[1] Follow the voice.\n[2] It must be monsters trying to bait me.\n")
    if choice == '1':
        moral.karma(NEUTRAL)
    elif choice == '2':
        player.timer_increase()
    else:
        print(INVALID)
        lost_forest()

def campsite1():
    if not game_on:
        return
    choice = input("You see a campsite.\n[1] Sit by the campsite (Heal)\n[2] You don't have time to waste.")
    if choice == '1':
        player.health_increase(30)
        player.timer_increase()
    elif choice == '2':
        pass
    else:
        print(INVALID)
        campsite1()

def field_of_bones():
    if not game_on:
        return
    choice = input("You stumbled across a field of bones. You can see corrupted slimes feasting on these bones. They will surely pose a threat to the nearby towns.\n[1] Combat the slimes.\n[2] The slimes won't make it to the next town.\n")
    if choice == '1':
        moral.karma(GOOD)
        combat(slime)
        combat(slime)
        player.timer_increase()
    elif choice == '2':
        print("You got ambushed on your way out!")
        moral.karma(EVIL)
        combat(slime)
        combat(slime)
        combat(slime)
        player.timer_increase()
    else:
        print(INVALID)
        field_of_bones()

def small_town():
    if not game_on:
        return
    choice = input("You have arrived at a small town. It is strangely empty. You hear some shuffling in the buildings around you.\n[1] Quick get away from the town.\n[2] Investigate.")
    if choice == '1':
        moral.karma(NEUTRAL)
    elif choice == '2':
        moral.karma(NEUTRAL)
        combat(skeleton)
        player.timer_increase()
    else:
        print(INVALID)
        small_town()

def campsite2():
    if not game_on:
        return
    choice = input("You see a campsite.\n[1] Sit by the campsite (Heal)\n[2] You don't have time to waste.")
    if choice == '1':
        player.health_increase(30)
        player.timer_increase()
    elif choice == '2':
        pass
    else:
        print(INVALID)
        campsite2()

def young_girl():
    if not game_on:
        return
    choice = input("You see a young girl in the distance. She seems very scared and anxious.\n[1] Help her out.\n[2] Ignore her.\n")
    if choice == '1':
        print("It was a trap! She separated into two slimes!")
        moral.karma(GOOD)
        player.timer_increase()
        combat(slime)
        combat(slime)
    elif choice == '2':
        moral.karma(EVIL)
    else:
        print(INVALID)
        young_girl()

def demon_book():
    if not game_on:
        return
    choice = input("You see a demonic book on the ground.\n[1] Read it.\n[2] It must be cursed.\n")
    if choice == '1':
        player.demon_knowledge = True
        player.timer_increase()
    elif choice == '2':
        moral.karma(NEUTRAL)
    else:
        print(INVALID)
        demon_book()

def thorny_road():
    if not game_on:
        return
    choice = input("You see a thorny road ahead of you. It will certainly hurt to go through it, but it will save you some time.\n[1] Go through the thorny road.\n[2] There must be a better option.\n")
    if choice == '1':
        player.health_decrease(30)
    elif choice == '2':
        player.timer_increase()
        player.timer_increase()
    else:
        print(INVALID)
        thorny_road()

def road_block():
    if not game_on:
        return
    choice = input("There is a giant road block in front of you. It is impossible to cross over it. You do see another way, but it is surrounded by goblins.\n [1] Enter Combat\n [2] Figure out another way.\n")
    if choice == '1':
        combat(goblin)
        combat(goblin)
    elif choice == '2':
        player.timer_increase()
    else:
        print(INVALID)
        road_block()

def campsite3():
    if not game_on:
        return
    choice = input("You see a campsite.\n[1] Sit by the campsite (Heal)\n[2] You don't have time to waste.")
    if choice == '1':
        player.health_increase(50)
        player.timer_increase()
    elif choice == '2':
        pass
    else:
        print(INVALID)
        campsite3()

def castle():
    if not game_on:
        return
    choice = input("You have arrived at the Demon King's castle. The front entrance is filled with monsters, while the back entrance is lightly guarded.\n[1] Storm through the front.\n[2] Sneak to the back entrance.\n")
    if choice == '1':
        combat(slime)
        combat(skeleton)
        combat(goblin)
    elif choice == '2':
        player.timer_increase()
        combat(skeleton)
    else:
        print(INVALID)
        castle()

def doorways():
    if not game_on:
        return
    choice = input("You managed to enter the castle. You see two different doorways.\n[1] Enter the left door.\n[2] Enter the right door.\n")
    if choice == '1':
        player.heal()
        print("You see a healing bath.\nYou have healed to full HP.\n")
    elif choice == '2':
        print("You ended up getting lost inside that room, wasting a lot of time.\n")
        player.timer_increase()
    else:
        print(INVALID)
        doorways()

def castle_map():
    if not game_on:
        return
    choice = input("You see a group a enemies that are holding a map of the castle. Having that map can greatly reduce the time needed to find the princess.\n[1] Enter combat.\n[2] You don't need a map.\n")
    if choice == '1':
        combat(goblin)
        combat(goblin)
        combat(slime)
        player.timer_decrease()
        player.timer_decrease()
        player.timer_decrease()
    elif choice == '2':
        moral.karma(NEUTRAL)
    else:
        print(INVALID)
        castle_map()

def ambush():
    if not game_on:
        return
    choice = input("You got stuck in a pincer trap. Enemies are surrounding you from both sides.\n[1] Enter Combat.\n[2] Bluff them.\n")
    if choice == '1':
        combat(slime)
        combat(skeleton)
        combat(goblin)
    elif choice == '2':
        if player.demon_knowledge:
            print("You use the knowledge from the demon book to convince the monster that you are one of the Demon King's subordinates.")
        else:
            print("Your bluff failed! You have to enter combat.")
            combat(slime)
            combat(skeleton)
            combat(goblin)
    else:
        print(INVALID)
        ambush()

def spare():
    if not game_on:
        return
    choice = input("You have successfully defeated the Demon King in combat. You now have the option to spare him or end his life.\n[1] Spare.\n[2] Kill.\n")
    if choice == '1':
        print("You decided to be merciful and spare the Demon King's life.")
        ending.convert_demon_king()
        moral.display()
    elif choice == '2':
        print("You decided that the Demon King must die.")
        if player.demon_knowledge:
            ending.secret_ending()
        else:
            ending.slay_demon_king()
            moral.display()
    else:
        print(INVALID)
        spare()

def throne_room():
    global game_on
    if not game_on:
        return
    choice = input("You have finally reached the Demon King. He states that he does not wish to fight you, instead, he offers you a high-ranking position in his army.\n[1] Refuse his offer and enter combat.\n[2] Join the Demon King.\n")
    if choice == '1':
        combat(demon_king)
        if player.health >= 1:
            spare()
        else:
            game_on = False
    elif choice == '2':
        print("You have decided to join forces with the Demon King. The future of the kingdom does not look bright.")
        ending.false_knight()
        moral.karma(EVIL)
        moral.karma(EVIL)
        moral.karma(EVIL)
        moral.display()
    else:
        print(INVALID)
        throne_room()











# Where the main code (driver) will run, this is currently a sample for Phase IV
while game_on:
    print('You just woke up underneath debris from your now destroyed home.\nYou barely remember who you are.')
    player.origin_selection()
    player.player_name()
    start_town()
    leave_town()
    kingdom_arrival()
    forest()
    fairy()
    lost_forest()
    campsite1()
    field_of_bones()
    small_town()
    campsite2()
    young_girl()
    demon_book()
    thorny_road()
    road_block()
    campsite3()
    castle()
    doorways()
    ambush()
    # Ending Selection

    if player.time >= 50:
        print("As you entered the throne room, you see that the princess has been transformed into a hideous monster.\nYou have failed your quest.")
        ending.too_late()
        moral.display()
        print('\nHint: You should select options that do not take much time.')
        game_on = False
    else:
        throne_room()


    game_on = False